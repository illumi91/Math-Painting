import os
from render_image import RenderImage
from unittest import mock
import webbrowser 


class TestSaveImage:
    
    def test_save(self, mocker):
        
        mock_open = mocker.patch.object(webbrowser, "open", autospec=True)
        render_image = RenderImage("test_image")
        render_image.render_image()
        
        mock_open.assert_called_once_with(
            "file://" + os.path.realpath("files/test_image.png")
        )
        