import torch

def export_onnx(model, path):
    """
    Export PyTorch model to ONNX format
    
    Args:
        model: PyTorch model to export
        path: Output path for ONNX file
    """
    dummy = torch.randn(1, 16000)
    torch.onnx.export(
        model, 
        dummy, 
        path,
        input_names=['audio'],
        output_names=['features'],
        dynamic_axes={'audio': {0: 'batch_size'}}
    )
