"""
Simple demo that generates avatar output without requiring audio files
"""
import numpy as np
import cv2
import torch
from pathlib import Path

def create_demo_audio():
    """Create a fake audio tensor for testing"""
    return torch.randn(1, 16000)  # Simulated audio

def generate_demo_avatar():
    """Generate a demo avatar frame"""
    print("🎬 Generating demo avatar...")
    
    # Create a simple colored frame as output
    frame = np.zeros((256, 256, 3), dtype=np.uint8)
    
    # Add a gradient background
    for i in range(256):
        frame[i, :] = [i, 128, 255 - i]
    
    # Add some text
    cv2.putText(frame, "Avatar Demo", (50, 128), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    return frame

def main():
    print("=" * 60)
    print("Avatar System - Demo Mode (No Audio Required)")
    print("=" * 60)
    
    # Generate demo output
    frame = generate_demo_avatar()
    
    # Save output
    output_path = Path("demo_output.png")
    cv2.imwrite(str(output_path), frame)
    
    print(f"✓ Demo avatar generated!")
    print(f"✓ Output saved to: {output_path.absolute()}")
    print("\n" + "=" * 60)
    print("To use with real audio:")
    print('  python main.py --audio "path/to/your/file.wav" --output result.png')
    print("=" * 60)

if __name__ == "__main__":
    main()
