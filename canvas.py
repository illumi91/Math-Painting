
from PIL import Image
import numpy as np

class Canvas:
    """
    Defines the canvas dimension and colour (black or white).
    """
    def __init__(self, width: float, height: float, colour: str):
        self.width = width
        self.height = height
        self.colour = colour
        
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        if self.colour == "black": 
            self.canvas[:] = [0, 0, 0]
        elif self.colour == "white":
            self.canvas[:] = [255, 255, 255]
        else: 
            raise ValueError(f"Invalid color: {self.colour}. Only 'black' and 'white' are allowed")

    def make(self, filename):
        pillow_image = Image.fromarray(self.canvas, "RGB")
        pillow_image.save(f"files/{filename}.png")