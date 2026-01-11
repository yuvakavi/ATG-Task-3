# Quick Reference Guide

## Common Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python test_workspace.py
```

### Usage
```bash
# Generate avatar from audio
python main.py --audio path/to/audio.wav --output result.png

# Start API server
python api/server.py

# Access API docs
# Visit: http://localhost:8000/docs
```

### Development
```bash
# Format code
black .

# Check linting
flake8 .

# Type checking
mypy .
```

### Optimization
```bash
# Export to ONNX
python -c "from optimization.onnx_export import export_onnx; from models.speech_encoder import SpeechEncoder; export_onnx(SpeechEncoder(), 'model.onnx')"

# Quantize model
python -c "from optimization.quantization import quantize; from models.speech_encoder import SpeechEncoder; quantize(SpeechEncoder())"
```

### Deployment
```bash
# Docker build
docker build -t avatar-system -f deployment/docker/Dockerfile .

# Docker run
docker run -p 8000:8000 --gpus all avatar-system

# Kubernetes deploy
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
```

## File Structure

```
avatar-system/
├── main.py                    # Main entry point
├── requirements.txt           # Dependencies
├── configs/                   # Configuration files
│   ├── model.yaml            # Model config
│   └── inference.yaml        # Inference config
├── models/                    # Neural network models
│   ├── speech_encoder/
│   ├── expression_model/
│   ├── motion_model/
│   └── renderer/
├── inference/                 # Pipeline implementation
│   ├── realtime_pipeline.py
│   └── temporal_filter.py
├── preprocessing/             # Audio preprocessing
│   ├── audio_cleaner.py
│   └── phoneme_extractor.py
├── optimization/              # Model optimization
│   ├── onnx_export.py
│   └── quantization.py
├── api/                       # REST API
│   ├── server.py
│   └── routes.py
├── evaluation/                # Metrics and benchmarking
├── deployment/                # Deployment configs
├── data/                      # Data directory
└── demo/                      # Demo applications
```

## Configuration

### Model Configuration (configs/model.yaml)
```yaml
speech_encoder: wav2vec2     # Speech encoding model
expression_model: transformer # Expression generation
motion_model: mlp            # Motion generation
renderer: neural             # Rendering method
fps: 30                      # Target framerate
```

### Inference Configuration (configs/inference.yaml)
```yaml
device: cuda                 # Device: cuda or cpu
precision: fp16              # Precision: fp16 or fp32
batch_size: 1                # Batch size for inference
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/health` | GET | Detailed status |
| `/generate` | POST | Generate avatar from audio |

## Troubleshooting

### Issue: Import errors
**Solution**: Ensure virtual environment is activated and dependencies installed

### Issue: CUDA not available
**Solution**: Install CUDA toolkit or use CPU mode (set `device: cpu` in config)

### Issue: Audio loading fails
**Solution**: Install ffmpeg, check audio format (WAV/MP3/FLAC)

### Issue: Model fails to load
**Solution**: Check file paths, verify model files exist

## Environment Variables

```bash
# Optional environment variables
export CUDA_VISIBLE_DEVICES=0    # Select GPU
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
```

## Performance Tips

1. **Use GPU**: Set `device: cuda` for 10-100× speedup
2. **Use FP16**: Set `precision: fp16` for 2× speedup
3. **Quantize**: Use INT8 quantization for 4× size reduction
4. **Batch Processing**: Increase batch_size for throughput
5. **ONNX Runtime**: Export to ONNX for optimized inference

## Support

- **Documentation**: See README.md and INSTALL.md
- **Issues**: Check CONTRIBUTING.md
- **Tests**: Run `python test_workspace.py`
