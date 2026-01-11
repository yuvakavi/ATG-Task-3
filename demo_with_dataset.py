"""Demo script using LJ Speech dataset"""
import argparse
import os
from data_loader import LJSpeechLoader
from inference.realtime_pipeline import run_pipeline
import cv2

def main():
    parser = argparse.ArgumentParser(description='Generate avatar from LJ Speech dataset')
    parser.add_argument('--dataset', type=str, 
                       default=r"C:\Users\Yuva sri\Downloads\lj-speech-dataset-master\lj-speech-dataset",
                       help='Path to LJ Speech dataset')
    parser.add_argument('--index', type=int, default=0,
                       help='Index of sample to use (default: 0)')
    parser.add_argument('--output', type=str, default='avatar_from_dataset.png',
                       help='Output image path')
    
    args = parser.parse_args()
    
    # Load dataset
    print(f"Loading LJ Speech dataset from: {args.dataset}")
    loader = LJSpeechLoader(args.dataset)
    print(f"Found {len(loader)} samples")
    
    if len(loader) == 0:
        print("Error: No samples found in dataset")
        return
    
    # Get sample
    sample = loader.get_sample(args.index)
    print(f"\nUsing sample {args.index}:")
    print(f"  Text: {sample['text']}")
    print(f"  Audio: {sample['audio_path']}")
    
    # Check if audio file exists
    if not os.path.exists(sample['audio_path']):
        print(f"\nWarning: Audio file not found at {sample['audio_path']}")
        print("You may need to run 'dvc pull' to download the audio files")
        print("\nFalling back to test audio...")
        sample['audio_path'] = 'data/audio_samples/test_sample.wav'
    
    # Run pipeline
    print(f"\nGenerating avatar...")
    try:
        frame = run_pipeline(sample['audio_path'])
        
        # Save output
        cv2.imwrite(args.output, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        print(f"✓ Avatar saved to: {args.output}")
        print(f"✓ Open the image to see the talking avatar!")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
