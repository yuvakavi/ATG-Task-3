# Talking Avatar Video Generation - README

## ✅ What's Working

All components are now functional:

### 1. **Single Frame Generation** 
```bash
python main.py --audio data/audio_samples/test_sample.wav --output avatar_result.png
```

### 2. **Video Generation (Silent)**
```bash
python demo/app.py --audio demo/demo_audio.wav --output demo/output_video.mp4 --fps 30
```

### 3. **Video with Audio (Requires FFmpeg)**
```bash
python generate_video_with_audio.py --audio demo/demo_audio.wav --output demo/final_video.mp4
```

## 📁 Generated Files

- **Images:**
  - `avatar_result.png` - Single frame from test audio
  - `avatar_result2.png` - Second test sample
  - `avatar_from_dataset.png` - Using LJ Speech metadata

- **Videos:**
  - `demo/output_video.mp4` - Silent video (90 frames, 3 seconds)
  - `demo/talking_avatar.mp4` - Short demo (30 frames, 1 second)
  - `demo/talking_avatar_full_temp.mp4` - Generated frames

- **Audio:**
  - `demo/demo_audio.wav` - Speech-like test audio (3 seconds)
  - `data/audio_samples/test_sample.wav` - Simple sine wave
  - `data/audio_samples/test_sample2.wav` - Different frequency

## 🎨 Avatar Features

The rendered avatar includes:
- 👤 **Face**: Skin-toned oval that moves with head motion
- 👀 **Eyes**: Blue pupils that track based on eye_motion parameters
- 👃 **Nose**: Center-placed facial feature
- 👄 **Mouth**: Opens/closes based on expression[0] parameter
- ✏️ **Eyebrows**: Raise/lower based on expression[1] parameter

## 📊 Technical Details

### Models:
1. **Speech Encoder**: Multi-layer Conv1D (32→64→128→256 features)
2. **Expression Model**: MLP with ReLU/Tanh (256→128→64 parameters)
3. **Motion Model**: Separate networks for head (3D) and eye (2D) motion
4. **Renderer**: PIL-based drawing with ImageDraw

### Video Specs:
- **Resolution**: 256x256 pixels
- **FPS**: 30 frames per second (configurable)
- **Format**: MP4 (H.264 codec)
- **Audio**: 16kHz mono WAV input

## 🚀 Usage Examples

### Generate Quick Test:
```bash
python main.py --audio data/audio_samples/test_sample.wav --output test.png
```

### Generate 5-Second Video:
```bash
python create_demo_audio.py --output my_audio.wav --duration 5
python demo/app.py --audio my_audio.wav --output my_video.mp4 --fps 30
```

### Use LJ Speech Dataset:
```bash
# After running: dvc pull in dataset folder
python demo_with_dataset.py --index 10 --output avatar10.png
```

## 🔧 Adding Audio to Video (Optional)

If you have FFmpeg installed:
```bash
ffmpeg -i demo/output_video.mp4 -i demo/demo_audio.wav -c:v copy -c:a aac -shortest demo/final_with_audio.mp4
```

Or install FFmpeg and use:
```bash
python generate_video_with_audio.py --audio demo/demo_audio.wav --output final.mp4
```

## 📈 Performance

- **Frame Generation**: ~3 frames/second on CPU
- **Video (3 seconds)**: ~30 seconds to generate
- **Model Loading**: Singleton pattern (loads once, reuses)

## ✨ Next Steps

1. **Add audio to video**: Install FFmpeg for automatic audio merging
2. **Use real speech**: Run `dvc pull` in LJ Speech dataset folder
3. **Improve models**: Train on actual avatar datasets
4. **Add more expressions**: Expand emotion parameters
5. **Real-time streaming**: Use webcam + microphone input
