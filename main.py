"""
Real-Time Talking Avatar System - Main Entry Point

This script runs the avatar generation pipeline from audio input.
"""
import argparse
import sys
from pathlib import Path
import cv2
import yaml

from inference.realtime_pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(description='Real-Time Talking Avatar System')
    parser.add_argument('--audio', type=str, required=True,
                       help='Path to input audio file')
    parser.add_argument('--output', type=str, default='output.png',
                       help='Path to output image file')
    parser.add_argument('--config', type=str, default='configs/inference.yaml',
                       help='Path to inference configuration file')
    
    args = parser.parse_args()
    
    # Check if audio file exists
    audio_path = Path(args.audio)
    if not audio_path.exists():
        print(f"Error: Audio file not found: {args.audio}")
        sys.exit(1)
    
    # Load inference config
    config_path = Path(args.config)
    if config_path.exists():
        with open(config_path) as f:
            config = yaml.safe_load(f)
        print(f"Loaded config: {config}")
    
    print(f"Processing audio: {args.audio}")
    print("Running pipeline...")
    
    try:
        # Run the avatar generation pipeline
        frame = run_pipeline(str(audio_path))
        
        # Save output frame
        cv2.imwrite(args.output, frame)
        print(f"✓ Output saved to: {args.output}")
        
    except Exception as e:
        print(f"Error during pipeline execution: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
