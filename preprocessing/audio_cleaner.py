import librosa
import numpy as np

def clean_audio(path):
    """
    Load and normalize audio file
    
    Args:
        path: Path to audio file
        
    Returns:
        audio: Normalized audio array sampled at 16kHz
    """
    audio, sr = librosa.load(path, sr=16000)
    # Normalize audio to [-1, 1] range
    audio = audio / (np.max(np.abs(audio)) + 1e-6)
    return audio
