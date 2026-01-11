# Installation and Setup Guide

## Prerequisites

- Python 3.8 or higher
- CUDA 11.8+ (for GPU acceleration)
- 8GB+ RAM (16GB recommended)
- GPU with 4GB+ VRAM (recommended: T4, V100, or A100)

## Installation Steps

### 1. Clone Repository

```bash
git clone <repository-url>
cd avatar-system
```

### 2. Set Up Python Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python test_workspace.py
```

## Configuration

### Model Configuration

Edit `configs/model.yaml`:
```yaml
speech_encoder: wav2vec2
expression_model: transformer
motion_model: mlp
renderer: neural
fps: 30
```

### Inference Configuration

Edit `configs/inference.yaml`:
```yaml
device: cuda  # or 'cpu'
precision: fp16  # or 'fp32'
batch_size: 1
```

## Quick Start

### Generate Avatar from Audio

```bash
python main.py --audio data/audio_samples/sample.wav --output result.png
```

### Start API Server

```bash
python api/server.py
```

Then visit: http://localhost:8000

### Run Tests

```bash
python test_workspace.py
```

## Troubleshooting

### CUDA Not Available

If you get "CUDA not available" errors:
1. Verify NVIDIA drivers are installed
2. Install CUDA toolkit matching your PyTorch version
3. Update `configs/inference.yaml` to use `device: cpu`

### Import Errors

If you get import errors:
1. Ensure virtual environment is activated
2. Verify all dependencies are installed
3. Check Python version (3.8+)

### Audio Loading Issues

If audio files fail to load:
1. Install ffmpeg: `sudo apt-get install ffmpeg` (Linux)
2. Ensure audio is in supported format (WAV, MP3, FLAC)
3. Check audio sample rate (16kHz recommended)

## Advanced Usage

### Export to ONNX

```python
from optimization.onnx_export import export_onnx
from models.speech_encoder import SpeechEncoder

model = SpeechEncoder()
export_onnx(model, "speech_encoder.onnx")
```

### Quantize Model

```python
from optimization.quantization import quantize
from models.speech_encoder import SpeechEncoder

model = SpeechEncoder()
quantized_model = quantize(model)
```

## Docker Deployment

See [deployment/docker/README.md](deployment/docker/README.md)

## Kubernetes Deployment

See [deployment/kubernetes/README.md](deployment/kubernetes/README.md)

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review error messages and logs
3. Ensure all dependencies are correctly installed
