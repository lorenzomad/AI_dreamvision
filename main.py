from craiyon import Craiyon

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout

import json
import os
 

class Content(MDBoxLayout):
    pass

save_path = 'save/save.json'
class Main(MDApp):
    """class that runs the dreamvision.kv file to visualize the frontend"""
    
       
    if os.path.exists(save_path):
        with open(save_path, "r") as r:
             save_data = json.load(r)
    else:
        save_data = {}

    dialog = None

    def build(self):
        return Builder.load_file("dreamvision.kv")

    def generate_dream(self):
        """generates dream images"""
        
        dream_description = self.root.dream_description.text
        dream_title = self.root.dream_title.text

        if dream_description != "" and dream_title != "":
            
            print("image generation started!\n dream used: " + dream_description )
            generator = Craiyon()
            result = generator.generate(dream_description)
            result.save_images()
            print("images generated")


            self.save_data[dream_title] = {
                "description": dream_description,
                "location": 'generated/image-1.png'
             }
            
            with open(save_path, "w") as p:
                json.dump(self.save_data, p)
            return result
        

dreamvision = Main()
dreamvision.run()


    