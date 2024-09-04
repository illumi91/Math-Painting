import numpy as np
from rectangle import Rectangle, Square


class TestRectangle:
    
    def test_draw_rectangle_between_bounds(self):
        canvas = np.zeros((100, 100, 3), dtype=np.uint8)
        rect = Rectangle(10, 10, 20, 30, "255", "0", "0")
        
        modified_canvas, _ = rect.draw(canvas)
        
        expected_colour = [255, 0, 0]
        assert np.all(modified_canvas[10:40, 10:30] == expected_colour)
        
    def test_draw_rectangle_out_of_bounds(self):
        canvas = np.zeros((50, 50, 3), dtype=np.uint8)
        rect = Rectangle(40, 40, 20, 20, '0', '255', '0')
        
        modified_canvas, _ = rect.draw(canvas)
        
        expected_color = [0, 255, 0]
        assert np.all(modified_canvas[40:50, 40:50] == expected_color)
        assert np.all(modified_canvas[40:50, 30:40] == [0, 0, 0])
        

class TestSquare:
    
    def test_draw_square_width_is_same_as_height(self):
        canvas = np.zeros((100, 100, 3), dtype=np.uint8)
        square = Square(x=10, y=10, width=25, red='255', green='0', blue='0')
        
        assert square.width == square.height == 25
        