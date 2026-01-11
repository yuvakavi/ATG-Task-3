"""LJ Speech Dataset Loader"""
import os
import csv
from pathlib import Path
from typing import List, Tuple

class LJSpeechLoader:
    """Loader for LJ Speech dataset"""
    
    def __init__(self, dataset_path: str):
        """
        Initialize LJ Speech loader
        
        Args:
            dataset_path: Path to LJ Speech dataset folder
        """
        self.dataset_path = Path(dataset_path)
        self.metadata_file = self.dataset_path / "metadata.csv"
        self.wavs_dir = self.dataset_path / "wavs"
        
        # Load metadata
        self.metadata = self._load_metadata()
        
    def _load_metadata(self) -> List[Tuple[str, str, str]]:
        """Load metadata from CSV file"""
        metadata = []
        
        if not self.metadata_file.exists():
            print(f"Warning: metadata.csv not found at {self.metadata_file}")
            return metadata
            
        with open(self.metadata_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                if len(row) >= 3:
                    file_id, text, normalized_text = row[0], row[1], row[2]
                    metadata.append((file_id, text, normalized_text))
                    
        return metadata
    
    def __len__(self) -> int:
        """Get number of samples"""
        return len(self.metadata)
    
    def get_audio_path(self, index: int) -> str:
        """Get audio file path for given index"""
        if index < 0 or index >= len(self.metadata):
            raise IndexError(f"Index {index} out of range [0, {len(self.metadata)})")
            
        file_id = self.metadata[index][0]
        audio_path = self.wavs_dir / f"{file_id}.wav"
        
        return str(audio_path)
    
    def get_text(self, index: int) -> Tuple[str, str]:
        """Get text and normalized text for given index"""
        if index < 0 or index >= len(self.metadata):
            raise IndexError(f"Index {index} out of range [0, {len(self.metadata)})")
            
        return self.metadata[index][1], self.metadata[index][2]
    
    def get_sample(self, index: int) -> dict:
        """Get complete sample (audio path and text) for given index"""
        audio_path = self.get_audio_path(index)
        text, normalized_text = self.get_text(index)
        
        return {
            'audio_path': audio_path,
            'text': text,
            'normalized_text': normalized_text,
            'file_id': self.metadata[index][0]
        }


if __name__ == "__main__":
    # Test the loader
    dataset_path = r"C:\Users\Yuva sri\Downloads\lj-speech-dataset-master\lj-speech-dataset"
    
    loader = LJSpeechLoader(dataset_path)
    print(f"Loaded {len(loader)} samples from LJ Speech dataset")
    
    if len(loader) > 0:
        sample = loader.get_sample(0)
        print(f"\nSample 0:")
        print(f"  File ID: {sample['file_id']}")
        print(f"  Audio path: {sample['audio_path']}")
        print(f"  Text: {sample['text']}")
        print(f"  Exists: {os.path.exists(sample['audio_path'])}")
