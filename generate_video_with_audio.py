"""
Generate talking avatar video with audio track using FFmpeg
"""
import argparse
import os
import subprocess
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from demo.app import generate_video


def generate_video_with_audio(audio_path: str, output_path: str, fps: int = 30):
    """
    Generate video with synced audio track
    
    Args:
        audio_path: Path to input audio file
        output_path: Path to output video file (with audio)
        fps: Frames per second
    """
    # Generate silent video first
    temp_video = output_path.replace('.mp4', '_temp.mp4')
    print("Step 1: Generating video frames...")
    generate_video(audio_path, temp_video, fps)
    
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        has_ffmpeg = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        has_ffmpeg = False
        print("\n⚠️  FFmpeg not found. Video will not have audio track.")
        print("    Install FFmpeg to add audio: https://ffmpeg.org/download.html")
        print(f"    Silent video saved as: {temp_video}")
        return
    
    # Combine video and audio using ffmpeg
    print("\nStep 2: Adding audio track with FFmpeg...")
    cmd = [
        'ffmpeg', '-y',
        '-i', temp_video,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-shortest',
        output_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Video with audio saved to: {output_path}")
            # Remove temp file
            os.remove(temp_video)
        else:
            print(f"⚠️  FFmpeg error: {result.stderr}")
            print(f"    Silent video available at: {temp_video}")
    except Exception as e:
        print(f"⚠️  Error combining audio: {e}")
        print(f"    Silent video available at: {temp_video}")


def main():
    parser = argparse.ArgumentParser(description='Generate talking avatar video with audio')
    parser.add_argument('--audio', type=str, required=True,
                       help='Input audio file path')
    parser.add_argument('--output', type=str, default='talking_avatar_with_audio.mp4',
                       help='Output video file path')
    parser.add_argument('--fps', type=int, default=30,
                       help='Frames per second (default: 30)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.audio):
        print(f"Error: Audio file not found: {args.audio}")
        return
    
    try:
        generate_video_with_audio(args.audio, args.output, args.fps)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
