# Open-Source Real-Time Talking Avatar System

This project generates a real-time talking avatar video from speech audio using fully open-source tools.

## Features
- Audio → Talking Avatar
- 30 FPS real-time pipeline
- Temporal stability
- GPU optimized (T4 / V100 / A100)
- FastAPI-based inference server

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### Run Pipeline
```bash
python main.py --audio data/audio_samples/sample.wav --output result.png
```

### Run API Server
```bash
python api/server.py
```

Then visit http://localhost:8000

## Project Structure

- `models/` - Neural network models (speech encoder, expression, motion, renderer)
- `inference/` - Real-time pipeline implementation
- `preprocessing/` - Audio cleaning and phoneme extraction
- `optimization/` - Model quantization and ONNX export
- `api/` - FastAPI server
- `configs/` - Configuration files
- `evaluation/` - Benchmarking tools
