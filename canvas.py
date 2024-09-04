import numpy as np

class Canvas:
    """
    Defines the canvas dimension and colour (black or white).
    """
    def __init__(self, width: float, height: float, colour: str):
        self.width = width
        self.height = height
        self.colour = colour
        
    def draw(self):
        canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        if self.colour == "black": 
            canvas[:] = [0, 0, 0]
        elif self.colour == "white":
            canvas[:] = [255, 255, 255]
        else: 
            raise ValueError(f"Invalid color: {self.colour}. Only 'black' and 'white' are allowed")
        
        return canvas
