#import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
 

#from kivy.uix.boxlayout import BoxLayout
import random

import main


class Main(MDApp):
    """class that runs the dreamvision.kv file to visualize the frontend"""
    
    dream_text = ObjectProperty(None)

    def build(self):
        return Builder.load_file("dreamvision.kv")

    def generate_dream(self):
        """generates a random number"""
        
        if self.root.dream_text.text != None:
            main.generate_dream(self.root.dream_text.text)
        
        
dreamvision = Main()
dreamvision.run()