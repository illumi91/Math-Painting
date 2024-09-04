import os
import webbrowser

class SaveImage:
    def __init__(self, filename: str):
        self.filename = filename
        
    def save(self, pillow_image):
        pillow_image.save(f"files/{self.filename}.png")
        
        webbrowser.open(
            "file://" + os.path.realpath(f"files/{self.filename}.png")
        )
