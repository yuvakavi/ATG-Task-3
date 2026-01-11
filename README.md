# Real-Time Talking Avatar System 🎭

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Open-Source Real-Time High-Quality Avatar System with Machine Learning/Deep Learning**

This project generates high-quality talking avatar videos from speech audio using fully open-source tools and deep learning models. Built as part of ATG Task 3 technical assignment.

## 🎯 Features

- 🎤 **Audio-to-Avatar Pipeline**: Convert speech to animated avatar
- 🚀 **Real-Time Capable**: 30 FPS generation (GPU-accelerated)
- 👤 **Realistic Rendering**: Face, eyes, nose, mouth, eyebrows with natural motion
- 🎬 **Video Generation**: Multiple format support (MP4, AVI, GIF)
- 🔧 **Production Ready**: Docker + Kubernetes deployment configs
- 📊 **Comprehensive Metrics**: Performance benchmarking and quality evaluation
- 🌐 **REST API**: FastAPI-based inference server

## 🏗️ Architecture

```
Audio Input (16kHz WAV)
    ↓
Speech Encoder (Conv1D) → 256-dim features
    ↓
Expression Model (MLP) → 64-dim expression params
    ↓
Motion Model (Separate nets) → Head (3D) + Eye (2D) motion
    ↓
Neural Renderer (PIL) → RGB Frame (256×256)
```

## 🎬 Demo Output

### Generated Avatar
![Avatar Demo](demo/avatar_demo.png)

### Video Generation
![Avatar Animation](demo/avatar_demo.gif)

*3-second talking avatar generated from speech-like audio at 30 FPS*

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yuvakavi/ATG-Task-3.git
cd ATG-Task-3

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## 🚀 Quick Start

### 1. Generate Test Audio
```bash
python create_demo_audio.py --output demo/demo_audio.wav --duration 3
```

### 2. Generate Single Frame
```bash
python main.py --audio demo/demo_audio.wav --output avatar.png
```

### 3. Generate Video
```bash
python demo/app.py --audio demo/demo_audio.wav --output demo/output.mp4 --fps 30
```

### 4. View Results
```bash
# Open interactive viewer in browser
cd demo
start viewer.html
```

## 📖 Advanced Usage

### Run Complete Pipeline
```bash
python main.py --audio your_audio.wav --output result.png
```

### Run API Server
```bash
python api/server.py
```
Then visit http://localhost:8000/docs for API documentation

### Generate Video with Audio Track (requires FFmpeg)
```bash
python generate_video_with_audio.py --audio demo_audio.wav --output final.mp4
```

### Use LJ Speech Dataset
```bash
python demo_with_dataset.py --index 0 --output avatar_sample.png
```

### Convert Video Formats
```bash
# To AVI (high compatibility)
python demo/convert_video.py --input video.mp4 --output video.avi --codec XVID

# To GIF (universal)
python demo/video_to_gif.py --input video.mp4 --output animation.gif
```

## 📁 Project Structure

```
avatar-system/
├── models/              # Neural network models
│   ├── speech_encoder/  # Audio feature extraction
│   ├── expression_model/# Expression parameter generation
│   ├── motion_model/    # Head and eye motion
│   └── renderer/        # Avatar frame rendering
├── inference/           # Real-time pipeline
├── preprocessing/       # Audio processing
├── api/                # FastAPI REST server
├── demo/               # Demo applications
├── evaluation/         # Metrics and benchmarking
├── deployment/         # Docker & Kubernetes configs
└── configs/            # YAML configurations
```

## 🎨 Avatar Features

The generated avatar includes:
- 👤 **Face**: Skin-toned oval with head motion
- 👀 **Eyes**: Animated pupils with gaze tracking
- 👃 **Nose**: Centered facial feature
- 👄 **Mouth**: Opens/closes based on speech
- ✏️ **Eyebrows**: Move with expression changes

## 📊 Technical Specifications

| Component | Details |
|-----------|---------|
| **Input** | 16kHz mono WAV audio |
| **Output** | 256×256 RGB frames @ 30 FPS |
| **Models** | PyTorch-based neural networks |
| **API** | FastAPI with async support |
| **Deployment** | Docker + Kubernetes ready |

## 📚 Documentation

- [Installation Guide](INSTALL.md) - Detailed setup instructions
- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Video Generation Guide](demo/VIDEO_README.md) - Create videos
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute
- [Changelog](CHANGELOG.md) - Version history

## 🧪 Testing

```bash
python test_workspace.py
```

## 📈 Performance

- **GPU (T4)**: ~30-60 FPS (real-time capable)
- **CPU (8 cores)**: ~5-10 FPS
- **Memory**: ~2GB GPU VRAM, ~4GB system RAM

## 🚀 Deployment

### Docker
```bash
cd deployment/docker
docker build -t avatar-system .
docker run -p 8000:8000 avatar-system
```

### Kubernetes
```bash
kubectl apply -f deployment/kubernetes/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- PyTorch team for deep learning framework
- OpenCV for image processing
- librosa for audio processing
- FastAPI for web framework

## 👨‍💻 Author

**Yuva Kavi**
- GitHub: [@yuvakavi](https://github.com/yuvakavi)
- Repository: [ATG-Task-3](https://github.com/yuvakavi/ATG-Task-3)

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Task**: ATG Task 3 - Technical Assignment  
**Date**: January 2026  
**Status**: ✅ Complete
