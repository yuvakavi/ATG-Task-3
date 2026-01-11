import torch
import torch.nn as nn

class ExpressionModel(nn.Module):
    """Expression model using transformer architecture (simplified)"""
    
    def __init__(self):
        super().__init__()
        # Multi-layer perceptron for expression generation
        self.fc1 = nn.Linear(256, 128)
        self.fc2 = nn.Linear(128, 64)
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()  # Output in [-1, 1] range
        self.dropout = nn.Dropout(0.1)
    
    def forward(self, features):
        """
        Generate expression parameters from speech features
        
        Args:
            features: Speech features [batch_size, 256]
            
        Returns:
            expression: Expression parameters [batch_size, 64]
        """
        x = self.relu(self.fc1(features))
        x = self.dropout(x)
        x = self.tanh(self.fc2(x))
        
        return x
