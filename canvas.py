
from PIL import Image
import numpy as np
from pathlib import Path

class Canvas():
    """
    Defines the canvas dimension and colour (black or white).
    """
    
    VALID_COLOURS = {
        "black": [0, 0, 0],
        "white": [255, 255, 255]
    }

    def __init__(self, width: int, height: int, colour: str):
        self.width = width
        self.height = height
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
