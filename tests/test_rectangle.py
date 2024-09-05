import numpy as np
from canvas import Canvas
from rectangle import Rectangle, Square


class TestRectangle:
    
    def test_draw_rectangle_between_bounds(self):
        canvas = Canvas(200, 100, "white")
        rect = Rectangle(10, 10, 20, 30, (255, 0, 0))
        
        rect.draw(canvas)
        
        expected_colour = (255, 0, 0)
        assert np.all(canvas.canvas[10:40, 10:30] == expected_colour)
        
    def test_draw_rectangle_out_of_bounds(self):
        canvas = Canvas(50, 50, "white")
        rect = Rectangle(40, 40, 20, 20, (0, 255, 0))
        
        rect.draw(canvas)
        
        expected_color = (0, 255, 0)
        assert np.all(canvas.canvas[40:50, 40:50] == expected_color)
        assert np.all(canvas.canvas[50:50, 30:40] == (0, 0, 0))
        

class TestSquare:
    
    def test_draw_square_width_is_same_as_height(self):
        canvas = Canvas(100, 100, "white")
        square = Square(x=10, y=10, width=25, colour=(255, 0, 0))
        
        assert square.width == square.height == 25
        