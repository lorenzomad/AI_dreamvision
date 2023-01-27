from craiyon import Craiyon

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
 

#from kivy.uix.boxlayout import BoxLayout
import random

import main


class Main(MDApp):
    """class that runs the dreamvision.kv file to visualize the frontend"""
    
    dream_text = ObjectProperty(None)

    data = {
        'Add dream': 'pencil'
    }

    def build(self):
        return Builder.load_file("dreamvision.kv")

    def generate_dream(self):
        """generates dream images"""
        
        if self.root.dream_text.text != None:
            
            print("image generation started!")
            generator = Craiyon()
            result = generator.generate(self.root.dream_text.text)
            result.save_images()
            print("images generated")
            return result
        
        
dreamvision = Main()
dreamvision.run()


    