"""
Demo application for the Real-Time Talking Avatar System

This script demonstrates the avatar system with video generation capabilities.
"""
import argparse
import os
import cv2
import numpy as np
import librosa
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from inference.realtime_pipeline import run_pipeline


def generate_video(audio_path: str, output_path: str, fps: int = 30):
    """
    Generate video from audio with talking avatar
    
    Args:
        audio_path: Path to input audio file
        output_path: Path to output video file
        fps: Frames per second for output video
    """
    print(f"Loading audio: {audio_path}")
    
    # Load audio
    audio, sr = librosa.load(audio_path, sr=16000)
    duration = len(audio) / sr
    total_frames = int(duration * fps)
    
    print(f"Audio duration: {duration:.2f}s, generating {total_frames} frames at {fps} FPS")
    
    # Generate first frame to get dimensions
    print("Generating frames...")
    first_frame = run_pipeline(audio_path)
    height, width = first_frame.shape[:2]
    
    # Create video writer with better codec compatibility
    # Try different codecs for better compatibility
    codecs = [
        ('avc1', 'H.264 (best compatibility)'),
        ('XVID', 'Xvid'),
        ('MJPG', 'Motion JPEG'),
        ('mp4v', 'MPEG-4')
    ]
    
    out = None
    for codec, name in codecs:
        try:
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            if out.isOpened():
                print(f"Using codec: {name}")
                break
        except:
            continue
    
    if out is None or not out.isOpened():
        # Fallback to default
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        raise RuntimeError(f"Failed to create video writer for {output_path}")
    
    # Calculate samples per frame
    samples_per_frame = int(sr / fps)
    
    # Generate video frame by frame
    for frame_idx in range(total_frames):
        # Extract audio segment for this frame
        start_sample = frame_idx * samples_per_frame
        end_sample = min(start_sample + 16000, len(audio))
        
        # Pad if needed
        audio_segment = audio[start_sample:start_sample + 16000]
        if len(audio_segment) < 16000:
            audio_segment = np.pad(audio_segment, (0, 16000 - len(audio_segment)))
        
        # Generate frame (using the full pipeline with audio variation)
        import torch
        from models import SpeechEncoder, ExpressionModel, MotionModel, Renderer
        
        # Initialize models (will use singleton cache)
        speech_encoder = SpeechEncoder()
        expression_model = ExpressionModel()
        motion_model = MotionModel()
        renderer = Renderer()
        
        speech_encoder.eval()
        expression_model.eval()
        motion_model.eval()
        
        # Process audio segment
        audio_tensor = torch.FloatTensor(audio_segment).unsqueeze(0)
        
        with torch.no_grad():
            # Extract features
            features = speech_encoder(audio_tensor)
            # Generate expression
            expression = expression_model(features)
            # Generate motion
            motion = motion_model(expression)
            # Render frame
            frame = renderer.render(expression, motion)
        
        # Convert RGB to BGR for OpenCV
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame_bgr)
        
        if (frame_idx + 1) % 30 == 0:
            print(f"  Generated {frame_idx + 1}/{total_frames} frames ({(frame_idx + 1) / total_frames * 100:.1f}%)")
    
    out.release()
    print(f"✓ Video saved to: {output_path}")
    print(f"✓ Duration: {duration:.2f}s, Resolution: {width}x{height}, FPS: {fps}")


def main():
    parser = argparse.ArgumentParser(description='Generate talking avatar video from audio')
    parser.add_argument('--audio', type=str, required=True,
                       help='Input audio file path')
    parser.add_argument('--output', type=str, default='output_video.mp4',
                       help='Output video file path')
    parser.add_argument('--fps', type=int, default=30,
                       help='Frames per second (default: 30)')
    
    args = parser.parse_args()
    
    # Validate input
    if not os.path.exists(args.audio):
        print(f"Error: Audio file not found: {args.audio}")
        return
    
    try:
        generate_video(args.audio, args.output, args.fps)
    except Exception as e:
        print(f"Error generating video: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
