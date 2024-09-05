import os
import webbrowser

class RenderImage:
    def __init__(self, filename: str):
        self.filename = filename
        
    def render_image(self):        
        webbrowser.open(
            "file://" + os.path.realpath(f"files/{self.filename}.png")
        )
