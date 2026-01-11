"""
Convert video to animated GIF for universal compatibility
"""
import cv2
import argparse
from pathlib import Path
from PIL import Image
import numpy as np


def video_to_gif(input_path: str, output_path: str, scale: float = 1.0, fps: int = None):
    """
    Convert video to animated GIF
    
    Args:
        input_path: Input video file
        output_path: Output GIF file
        scale: Scale factor (0.5 = half size)
        fps: FPS for GIF (None = use original)
    """
    print(f"Converting {input_path} to GIF")
    
    # Open video
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print(f"Error: Cannot open video: {input_path}")
        return False
    
    # Get properties
    original_fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if fps is None:
        fps = original_fps
    
    # Calculate new size
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    print(f"Input: {width}x{height}, {original_fps} FPS, {total_frames} frames")
    print(f"Output: {new_width}x{new_height}, {fps} FPS")
    
    # Read all frames
    frames = []
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Resize if needed
        if scale != 1.0:
            frame_rgb = cv2.resize(frame_rgb, (new_width, new_height))
        
        # Convert to PIL Image
        img = Image.fromarray(frame_rgb)
        frames.append(img)
        
        frame_count += 1
        if frame_count % 30 == 0:
            print(f"  Read {frame_count}/{total_frames} frames")
    
    cap.release()
    
    if not frames:
        print("Error: No frames extracted")
        return False
    
    # Calculate duration per frame in milliseconds
    duration = int(1000 / fps)
    
    # Save as GIF
    print(f"Saving GIF with {len(frames)} frames...")
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=False
    )
    
    file_size = Path(output_path).stat().st_size / 1024 / 1024
    print(f"✓ GIF created: {output_path}")
    print(f"  Size: {file_size:.2f} MB")
    return True


def main():
    parser = argparse.ArgumentParser(description='Convert video to animated GIF')
    parser.add_argument('--input', type=str, default='talking_avatar.mp4',
                       help='Input video file')
    parser.add_argument('--output', type=str, default='talking_avatar.gif',
                       help='Output GIF file')
    parser.add_argument('--scale', type=float, default=1.0,
                       help='Scale factor (default: 1.0, use 0.5 for smaller file)')
    parser.add_argument('--fps', type=int, default=None,
                       help='FPS for GIF (default: same as input)')
    
    args = parser.parse_args()
    
    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        return
    
    video_to_gif(args.input, args.output, args.scale, args.fps)


if __name__ == "__main__":
    main()
