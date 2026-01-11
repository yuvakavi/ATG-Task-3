import torch
import numpy as np
from PIL import Image, ImageDraw

class Renderer:
    def __init__(self):
        """Initialize the neural renderer"""
        self.resolution = (256, 256)
    
    def render(self, expression, motion):
        """
        Render avatar frame from expression and motion parameters
        
        Args:
            expression: Expression features tensor [batch, 64]
            motion: Motion parameters tuple (head_motion [batch, 3], eye_motion [batch, 2])
            
        Returns:
            frame: RGB image as numpy array [H, W, 3]
        """
        # Convert tensors to numpy
        if torch.is_tensor(expression):
            expression = expression.detach().cpu().numpy()[0]
        
        # Handle motion as either tuple or concatenated tensor
        if isinstance(motion, tuple):
            head_motion = motion[0].detach().cpu().numpy()[0] if torch.is_tensor(motion[0]) else motion[0]
            eye_motion = motion[1].detach().cpu().numpy()[0] if torch.is_tensor(motion[1]) else motion[1]
        else:
            if torch.is_tensor(motion):
                motion = motion.detach().cpu().numpy()[0]
            head_motion = motion[:3]
            eye_motion = motion[3:5]
        
        # Create canvas with skin tone background
        img = Image.new('RGB', self.resolution, color=(240, 220, 200))
        draw = ImageDraw.Draw(img)
        
        # Extract motion parameters
        head_yaw = head_motion[1] if len(head_motion) > 1 else 0
        head_pitch = head_motion[0] if len(head_motion) > 0 else 0
        eye_x = eye_motion[0] if len(eye_motion) > 0 else 0
        eye_y = eye_motion[1] if len(eye_motion) > 1 else 0
        
        # Face center with head motion
        center_x = 128 + int(head_yaw * 20)
        center_y = 128 + int(head_pitch * 20)
        
        # Draw face (circle)
        face_radius = 80
        draw.ellipse([
            center_x - face_radius, center_y - face_radius,
            center_x + face_radius, center_y + face_radius
        ], fill=(255, 220, 180), outline=(200, 160, 120), width=3)
        
        # Draw eyes based on eye motion
        eye_offset_x = int(eye_x * 10)
        eye_offset_y = int(eye_y * 10)
        
        # Left eye
        left_eye_x = center_x - 30 + eye_offset_x
        left_eye_y = center_y - 20 + eye_offset_y
        draw.ellipse([left_eye_x - 10, left_eye_y - 8, 
                     left_eye_x + 10, left_eye_y + 8], 
                    fill=(255, 255, 255), outline=(0, 0, 0), width=2)
        draw.ellipse([left_eye_x - 5, left_eye_y - 5, 
                     left_eye_x + 5, left_eye_y + 5], 
                    fill=(50, 50, 200))
        
        # Right eye
        right_eye_x = center_x + 30 + eye_offset_x
        right_eye_y = center_y - 20 + eye_offset_y
        draw.ellipse([right_eye_x - 10, right_eye_y - 8, 
                     right_eye_x + 10, right_eye_y + 8], 
                    fill=(255, 255, 255), outline=(0, 0, 0), width=2)
        draw.ellipse([right_eye_x - 5, right_eye_y - 5, 
                     right_eye_x + 5, right_eye_y + 5], 
                    fill=(50, 50, 200))
        
        # Draw nose
        nose_x = center_x
        nose_y = center_y + 10
        draw.ellipse([nose_x - 8, nose_y - 5, 
                     nose_x + 8, nose_y + 15], 
                    fill=(220, 180, 140))
        
        # Draw mouth with expression-based opening
        mouth_open = abs(expression[0]) * 30
        mouth_y = center_y + 40
        
        if mouth_open > 0.3:
            # Open mouth (talking)
            draw.ellipse([center_x - 25, mouth_y - 10, 
                         center_x + 25, mouth_y + int(mouth_open)], 
                        fill=(180, 80, 80), outline=(150, 50, 50), width=2)
        else:
            # Closed mouth (smile)
            draw.arc([center_x - 25, mouth_y - 10, 
                     center_x + 25, mouth_y + 10], 
                    start=0, end=180, fill=(150, 50, 50), width=3)
        
        # Draw eyebrows with expression
        eyebrow_raise = expression[1] * 10 if len(expression) > 1 else 0
        
        # Left eyebrow
        draw.arc([left_eye_x - 15, left_eye_y - 20 - int(eyebrow_raise), 
                 left_eye_x + 15, left_eye_y - 10 - int(eyebrow_raise)], 
                start=0, end=180, fill=(100, 70, 50), width=3)
        
        # Right eyebrow
        draw.arc([right_eye_x - 15, right_eye_y - 20 - int(eyebrow_raise), 
                 right_eye_x + 15, right_eye_y - 10 - int(eyebrow_raise)], 
                start=0, end=180, fill=(100, 70, 50), width=3)
        
        # Convert to numpy array
        return np.array(img)
