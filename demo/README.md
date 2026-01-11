# Demo Outputs

This folder contains example outputs from the avatar system.

## 📁 Files

### Audio Samples
- **demo_audio.wav** - 3-second speech-like audio (16kHz, generated)

### Image Outputs
- **avatar_sample.png** - Avatar generated from demo_audio.wav
- **example_output1.png** - Avatar from test_sample.wav (440Hz tone)
- **example_output2.png** - Avatar from test_sample2.wav (523Hz tone)

### Video Outputs
- **talking_avatar.mp4** - 3-second video (90 frames @ 30 FPS, 256×256)
- **talking_avatar.gif** - Animated version (192×192, 0.65 MB)

## 🎨 Avatar Features Shown

Each output demonstrates:
- 👤 Skin-toned face with natural shape
- 👀 Blue eyes with animated pupils
- 👃 Center-placed nose
- 👄 Mouth opening/closing based on audio
- ✏️ Eyebrows moving with expression
- 🎯 Head and eye motion based on audio features

## 🚀 Regenerate Examples

```bash
# Create audio
python create_demo_audio.py --output demo/demo_audio.wav --duration 3

# Generate image
python main.py --audio demo/demo_audio.wav --output demo/avatar_sample.png

# Generate video
python demo/app.py --audio demo/demo_audio.wav --output demo/talking_avatar.mp4 --fps 30

# Create GIF
python demo/video_to_gif.py --input demo/talking_avatar.mp4 --output demo/talking_avatar.gif
```

## 📊 Specifications

| File | Size | Format | Resolution | Duration |
|------|------|--------|------------|----------|
| demo_audio.wav | ~96 KB | WAV 16kHz | - | 3s |
| avatar_sample.png | ~15 KB | PNG | 256×256 | - |
| talking_avatar.mp4 | ~80 KB | MP4 H.264 | 256×256 | 3s @ 30fps |
| talking_avatar.gif | ~650 KB | GIF | 192×192 | 3s @ 30fps |

## 🌐 View in Browser

Open [viewer.html](viewer.html) in a web browser to see all outputs with interactive controls.
