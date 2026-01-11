import torch
import torch.nn as nn
import numpy as np

class SpeechEncoder(nn.Module):
    """Speech encoder using wav2vec2 architecture (simplified)"""
    
    def __init__(self):
        super().__init__()
        # Multi-layer feature extraction
        self.conv1 = nn.Conv1d(1, 32, kernel_size=10, stride=5)
        self.conv2 = nn.Conv1d(32, 64, kernel_size=8, stride=4)
        self.conv3 = nn.Conv1d(64, 128, kernel_size=4, stride=2)
        self.fc = nn.Linear(128, 256)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.1)
    
    def forward(self, audio):
        """
        Encode audio to feature vectors
        
        Args:
            audio: Input audio tensor [batch_size, 16000]
            
        Returns:
            features: Encoded features [batch_size, 256]
        """
        # Reshape for conv1d: [batch, channels, samples]
        x = audio.unsqueeze(1)
        
        # Convolutional feature extraction
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        
        # Global average pooling
        x = torch.mean(x, dim=2)
        
        # Fully connected layer
        x = self.dropout(self.fc(x))
        
        return x
