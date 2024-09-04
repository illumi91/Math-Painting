import numpy as np
from PIL import Image

class Rectangle:
    """
    Rectangle shape defined given x and y coordinates, 
    dimensions and colour in RGB format.
    """
    def __init__(self, x: float, y: float, width: float, height: float, red: str, green: str, blue: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.red = red
        self.green = green
        self.blue = blue
    
    def draw(self, canvas: np.ndarray):
        canvas[self.y:self.y + self.height, self.x:self.x + self.width] = [self.red, self.green, self.blue]
        pillow_image = Image.fromarray(canvas, "RGB")
        
        return canvas, pillow_image


class Square(Rectangle):
    """
    Square shape which is a particular rectangle.
    """
    def __init__(self, x, y, width, red, green, blue):
        super().__init__(x, y, width, width, red, green, blue)
        

