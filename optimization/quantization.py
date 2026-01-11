import torch

def quantize(model):
    """
    Quantize model to reduce size and improve inference speed
    
    Args:
        model: PyTorch model to quantize
        
    Returns:
        Quantized model
    """
    return torch.quantization.quantize_dynamic(
        model, {torch.nn.Linear}, dtype=torch.qint8
    )
