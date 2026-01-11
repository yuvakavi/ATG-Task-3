"""
Setup script to create test audio files for the avatar system
"""
import numpy as np
import soundfile as sf
from pathlib import Path

def create_test_audio_files():
    """Create test audio files in the data/audio_samples directory"""
    
    # Create directory if it doesn't exist
    audio_dir = Path("data/audio_samples")
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    print("🎵 Creating test audio files...")
    
    # Create a simple sine wave audio (1 second at 16kHz)
    sample_rate = 16000
    duration = 1.0
    frequency = 440  # A4 note
    
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = np.sin(2 * np.pi * frequency * t) * 0.3
    
    # Save as WAV file
    output_path = audio_dir / "test_sample.wav"
    sf.write(output_path, audio, sample_rate)
    
    print(f"✓ Created: {output_path}")
    
    # Create a second test file with different frequency
    frequency2 = 523.25  # C5 note
    audio2 = np.sin(2 * np.pi * frequency2 * t) * 0.3
    output_path2 = audio_dir / "test_sample2.wav"
    sf.write(output_path2, audio2, sample_rate)
    
    print(f"✓ Created: {output_path2}")
    
    print("\n✅ Test audio files created successfully!")
    print("\nNow you can run:")
    print('  python main.py --audio data/audio_samples/test_sample.wav --output result.png')
    
    return output_path

if __name__ == "__main__":
    try:
        create_test_audio_files()
    except ImportError as e:
        print("❌ Error: Missing dependency")
        print(f"   {e}")
        print("\nPlease install soundfile:")
        print("   pip install soundfile")
