import os
from save_image import SaveImage
from unittest import mock
import pytest 


class TestSaveImage:
    
    def test_save(self, mocker):
        pillow_image = mocker.patch("PIL.Image.Image", autospec=True)
        
        with mock.patch("webbrowser.open") as mock_open:
            save_image = SaveImage("test_image")
            save_image.save(pillow_image)
            
            pillow_image.save.assert_called_once_with("files/test_image.png")
            
            mock_open.assert_called_once_with(
                "file://" + os.path.realpath("files/test_image.png")
            )
        