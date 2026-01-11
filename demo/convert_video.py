"""
Convert video to different formats for better compatibility
"""
import cv2
import argparse
from pathlib import Path


def convert_video(input_path: str, output_path: str, codec: str = 'XVID'):
    """
    Convert video to different codec/format
    
    Args:
        input_path: Input video file
        output_path: Output video file
        codec: Codec to use (XVID, MJPG, avc1, mp4v)
    """
    print(f"Converting {input_path} to {output_path}")
    print(f"Using codec: {codec}")
    
    # Open input video
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print(f"Error: Cannot open video file: {input_path}")
        return False
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Input: {width}x{height}, {fps} FPS, {total_frames} frames")
    
    # Create output video writer
    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        print(f"Error: Cannot create output video with codec {codec}")
        cap.release()
        return False
    
    # Copy frames
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        out.write(frame)
        frame_count += 1
        
        if frame_count % 30 == 0:
            print(f"  Processed {frame_count}/{total_frames} frames ({frame_count/total_frames*100:.1f}%)")
    
    cap.release()
    out.release()
    
    print(f"✓ Conversion complete: {output_path}")
    print(f"  Processed {frame_count} frames")
    return True


def main():
    parser = argparse.ArgumentParser(description='Convert video to different format')
    parser.add_argument('--input', type=str, default='output_video.mp4',
                       help='Input video file')
    parser.add_argument('--output', type=str, default='output_video_converted.avi',
                       help='Output video file')
    parser.add_argument('--codec', type=str, default='XVID',
                       choices=['XVID', 'MJPG', 'mp4v', 'avc1'],
                       help='Codec to use (default: XVID)')
    
    args = parser.parse_args()
    
    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        return
    
    convert_video(args.input, args.output, args.codec)


if __name__ == "__main__":
    main()
