import numpy as np
from canvas import Canvas
import pytest

class TestCanvas:

    def test_draw_black_canvas(self):
        canvas = Canvas(4, 1, "black")
        
        canvas_colour = canvas.draw()
        
        expected_result = np.array([[[0, 0, 0],
                                     [0, 0, 0],
                                     [0, 0, 0],
                                     [0, 0, 0]]], dtype=np.uint8)
        
        assert np.array_equal(canvas_colour, expected_result)
        
    def test_draw_white_canvas(self):
        canvas = Canvas(4, 1, "white")
        
        canvas_colour = canvas.draw()
        
        expected_result = np.array([[[255, 255, 255],
                                     [255, 255, 255],
                                     [255, 255, 255],
                                     [255, 255, 255]]], dtype=np.uint8)
        
        assert np.array_equal(canvas_colour, expected_result)
        
    def test_draw_invalid_colour(self):
        canvas = Canvas(4, 1, "invalid")
        
        with pytest.raises(ValueError):
            canvas.draw()
                            
    