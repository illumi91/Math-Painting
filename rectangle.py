from canvas import Canvas
import numpy as np

class Rectangle:
    """
    Rectangle shape defined given x and y coordinates, 
    dimensions and colour in RGB format.
    """
    def __init__(self, x: int, y: int, width: int, height: int, colour: tuple):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    
    def draw(self, canvas: Canvas):
        canvas.canvas[self.y:self.y + self.height, self.x:self.x + self.width] = (self.colour)


class Square(Rectangle):
    """
    Square shape which is a particular rectangle.
    """
    def __init__(self, x, y, width, colour):
        super().__init__(x, y, width, width, colour)
        

