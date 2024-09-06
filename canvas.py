
from PIL import Image
import numpy as np
from pathlib import Path

class Canvas:
    """
    Defines the canvas dimension and colour (black or white).
    """
    
    VALID_COLOURS = {
        "black": [0, 0, 0],
        "white": [255, 255, 255]
    }

    def __init__(self, width: int, height: int, colour: str):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width and height must be numbers.")
        if width <= 0 or height <= 0:
            raise ValueError("Widht adn height must be positive numbers.")
        
        self.width = width
        self.height = height
        
        if colour not in self.VALID_COLOURS:
            raise ValueError(f"Invalid colour: {colour}. Only 'black' and 'white' are allowed.")
        self.colour = self.VALID_COLOURS[colour]
        
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def make(self, filename: str, directory: str = "files"):
        """
        Save the canvas as an image file.
        """
        directory_path = Path(directory)
        filepath = directory_path / f"{filename}.png"

        pillow_image = Image.fromarray(self.canvas, "RGB")
        pillow_image.save(filepath)
        print(f"Image saved at {filepath}")
