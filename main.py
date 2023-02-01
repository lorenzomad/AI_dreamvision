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
import sqlite3
import sql_functions

save_path = 'save/save.json'

def import_save(save_path):
    """imports the saved data from an existing json file into a dictionary"""
    if os.path.exists(save_path):
        with open(save_path, "r") as r:
             save_data = json.load(r)
    else:
        save_data = {}
    return save_data

def create_image(prompt):
    """generates image from the defined prompt"""
    print("Image generation started! \nDream used: " + prompt)
    generator = Craiyon()
    result = generator.generate("a dream where " + prompt)
    images = result.images
    print("Images generated successfully!")
    image_data = base64.b64decode(images[0].replace(" ", "+"))
    return image_data
 
def save_image(image_data, save_file, folder_name, title, description):
    """saves the image to save_file to the defined folder name in a /jpg format """
    file_name = folder_name + title.replace(" ", "_") + ".jpg" 
    #append [1] if the file name exists
    while(os.path.exists(file_name)):
        file_name += '[1]'
    #write image file to disk
    with open(file_name, 'wb') as f:
        f.write(image_data)
    #write result
    save_data = import_save(save_file)
    save_data[title] = {
        "description": description,
        "location": file_name
        }
    with open(save_file, "w") as p:
        json.dump(save_data, p)
    return save_data

class Gallery_entry(TwoLineAvatarIconListItem):
    # kv custom object to visualize one dream entry
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    icon = StringProperty("")
    image_source = StringProperty("")


class Main(MDApp):
    """frontend building class"""

    #Import save file  
    save_data = import_save(save_path)
    
    def build(self):
        return Builder.load_file("dreamvision.kv")
        

    def generate_dream(self):
        """generates dream images"""
        dream_description = self.root.dream_description.text
        dream_title = self.root.dream_title.text
        self.load_main_image()

        if dream_description != "" and dream_title != "":
            image_data = create_image(dream_description)
            self.save_data = save_image(
                image_data,
                save_path,
                'generated/', 
                dream_title, 
                dream_description)

    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        # date_dialog.bind(on_save=self.on_save)
        # date_dialog.open()

    def load_main_image(self):
        """function to load one image"""
        if len(self.save_data) != 0:
            self.root.main_image.source = list(self.save_data.values())[0]["location"]

    def load_gallery(self):
        """function to generate the images in the gallery at launch of the screen"""
        # delete pre-existing widgets
        self.root.ids['gallery'].clear_widgets()
        # generates image line items
        for title in self.save_data:
            self.root.ids['gallery'].add_widget(
                Gallery_entry(text=title, 
                secondary_text = self.save_data[title]["description"],
                image_source = self.save_data[title]["location"],
                icon = 'delete'
                )
            )
        

#connect db
sql_functions.create_db("dreams.db", "schema.sql")
dreamvision = Main()
dreamvision.run()


    