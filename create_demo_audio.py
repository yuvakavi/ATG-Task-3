"""
Create demo audio file with varied speech-like tones
"""
import numpy as np
import soundfile as sf
import argparse

def create_speech_like_audio(output_path: str, duration: float = 3.0):
    """Create a more speech-like audio with varying frequencies"""
    
    sample_rate = 16000
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create varied tones that mimic speech patterns
    audio = np.zeros_like(t)
    
    # Add fundamental frequency and harmonics
    frequencies = [
        (200, 0.3),   # Base frequency
        (400, 0.2),   # First harmonic
        (600, 0.15),  # Second harmonic
        (300, 0.1),   # Variation
    ]
    
    # Add frequency modulation to simulate speech
    for i, (freq, amp) in enumerate(frequencies):
        # Vary frequency over time
        freq_mod = freq + 50 * np.sin(2 * np.pi * 0.5 * t * (i + 1))
        audio += amp * np.sin(2 * np.pi * freq_mod * t)
    
    # Add amplitude envelope (speech-like)
    envelope = 0.5 + 0.5 * np.sin(2 * np.pi * 2 * t)
    audio = audio * envelope
    
    # Normalize
    audio = audio / np.max(np.abs(audio)) * 0.7
    
    # Save
    sf.write(output_path, audio, sample_rate)
    print(f"✓ Created speech-like audio: {output_path}")
    print(f"  Duration: {duration}s, Sample rate: {sample_rate}Hz")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create demo audio file')
    parser.add_argument('--output', type=str, default='demo/demo_audio.wav',
                       help='Output audio file path')
    parser.add_argument('--duration', type=float, default=3.0,
                       help='Duration in seconds (default: 3.0)')
    
    args = parser.parse_args()
    create_speech_like_audio(args.output, args.duration)
