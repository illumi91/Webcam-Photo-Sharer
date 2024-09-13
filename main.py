from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from pathlib import Path

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        """
        Starts camera and changes Button text
        """
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
    
    def stop(self):
        """
        Stops camera and changes Button text
        """
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
    
    def capture(self):
        """
        Creates a filename with the current time and captures
        and saves a photo image under that filename
        """
        directory = Path("images")
        directory.mkdir(exist_ok=True)
        current_time = time.strftime("%Y%m%d-%H%M%S")
        filepath = str(directory.joinpath(current_time + ".png"))
        self.ids.camera.export_to_png(filepath)
        
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath

class ImageScreen(Screen):
    def create_link(self):
        


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    
    def build(self):
        return RootWidget()
    
    
MainApp().run()