import torch
import torch.nn as nn

class MotionModel(nn.Module):
    """Motion model using MLP architecture"""
    
    def __init__(self):
        super().__init__()
        # Separate networks for different motion types
        self.head_net = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 3)  # pitch, yaw, roll
        )
        self.eye_net = nn.Sequential(
            nn.Linear(64, 16),
            nn.ReLU(),
            nn.Linear(16, 2)  # eye_x, eye_y
        )
        self.tanh = nn.Tanh()  # Limit motion range
    
    def forward(self, expression):
        """
        Generate motion parameters from expression
        
        Args:
            expression: Expression parameters [batch_size, 64]
            
        Returns:
            head_motion: Head motion parameters [batch_size, 3]
            eye_motion: Eye motion parameters [batch_size, 2]
        """
        # Generate head motion
        head_motion = self.tanh(self.head_net(expression)) * 0.3  # Small head movements
        
        # Generate eye motion
        eye_motion = self.tanh(self.eye_net(expression)) * 0.5  # Moderate eye movements
        
        return head_motion, eye_motion
