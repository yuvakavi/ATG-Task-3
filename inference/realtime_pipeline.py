import torch
import yaml
from pathlib import Path
from preprocessing.audio_cleaner import clean_audio
from models.speech_encoder import SpeechEncoder
from models.expression_model import ExpressionModel
from models.motion_model import MotionModel
from models.renderer import Renderer

# Load models globally (singleton pattern)
_models = None

def _get_models():
    global _models
    if _models is None:
        # Load configuration
        config_path = Path(__file__).parent.parent / "configs" / "model.yaml"
        with open(config_path) as f:
            config = yaml.safe_load(f)
        
        _models = {
            'speech': SpeechEncoder(),
            'expression': ExpressionModel(),
            'motion': MotionModel(),
            'renderer': Renderer()
        }
    return _models

def run_pipeline(audio_path):
    audio = clean_audio(audio_path)
    
    # Ensure audio has correct shape [batch_size, sequence_length]
    # clean_audio returns 1D array, need to match expected input of 16000
    if len(audio) < 16000:
        # Pad if too short
        audio = torch.nn.functional.pad(torch.tensor(audio), (0, 16000 - len(audio)))
    else:
        # Truncate if too long
        audio = torch.tensor(audio[:16000])
    
    audio = audio.unsqueeze(0).float()  # Add batch dimension [1, 16000]

    models = _get_models()
    
    features = models['speech'](audio)
    expression = models['expression'](features)
    head_motion, eye_motion = models['motion'](expression)
    frame = models['renderer'].render(expression, head_motion)

    return frame
