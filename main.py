from craiyon import Craiyon

#kivy imports
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.properties import StringProperty

#general imports
import json
import os
import base64
from io import BytesIO

 
class ListItemWithImage(TwoLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    icon = StringProperty("")
    image_source = StringProperty("")


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
            
            print("Image generation started! \nDream used: " + dream_description )
            generator = Craiyon()
            result = generator.generate("a dream where " + dream_description)
            images = result.images
            print("Images generated successfully!")

            condensed_title = dream_title.replace(" ", "") 
            image_data = base64.b64decode(images[0].replace(" ", "+"))
            
            file_name = 'generated/' + condensed_title + ".jpg" 
            
            while(os.path.exists(file_name)):
                file_name += '[1]'
                
            
            with open(file_name, 'wb') as f:
                f.write(image_data)

            
            self.save_data[dream_title] = {
                "description": dream_description,
                "location": file_name
             }
            
            with open(save_path, "w") as p:
                json.dump(self.save_data, p)
            return result

    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        # date_dialog.bind(on_save=self.on_save)
        # date_dialog.open()

    def load_main_image(self):
        self.root.main_image.source = list(self.save_data.values())[0]["location"]

    def load_gallery(self):
        """function to generate the images in the gallery at launch of the screen"""

        for title in self.save_data:
            
            self.root.ids['gallery'].add_widget(
                ListItemWithImage(text=title, 
                secondary_text = self.save_data[title]["description"],
                image_source = self.save_data[title]["location"],
                icon = 'delete'
                )
            )
        

dreamvision = Main()
dreamvision.run()


    