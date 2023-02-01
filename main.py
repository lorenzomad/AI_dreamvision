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
from datetime import date

# save_path = 'save/save.json'

# def import_save(save_path):
#     """imports the saved data from an existing json file into a dictionary"""
#     if os.path.exists(save_path):
#         with open(save_path, "r") as r:
#              save_data = json.load(r)
#     else:
#         save_data = {}
#     return save_data

def create_image(prompt):
    """generates image from the defined prompt"""
    print("Image generation started! \nDream used: " + prompt)
    generator = Craiyon()
    result = generator.generate("a dream where " + prompt)
    images = result.images
    print("Images generated successfully!")
    image_data = base64.b64decode(images[0].replace(" ", "+"))
    return image_data
 
def save_image(image_data, folder_name, title):
    """saves the image to the defined folder name in a .jpg format """
    file_name = folder_name + '/' + title.lower().replace(" ", "_") + ".jpg" 
    #append [1] if the file name exists
    while(os.path.exists(file_name)):
        file_name = file_name + '(1)'
    #write image file to disk
    with open(file_name, 'wb') as f:
        f.write(image_data)

class Gallery_entry(TwoLineAvatarIconListItem):
    # kv custom object to visualize one dream entry
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    icon = StringProperty("")
    image_source = StringProperty("")


class Main(MDApp):
    """frontend building class"""

    #Import save file  
    # save_data = import_save(save_path)
    #connect db
    connection = sqlite3.connect("dreams.db")
    cursor = connection.cursor()
    sql_functions.create_db(connection, "schema.sql")
    
    
    def build(self):
        return Builder.load_file("dreamvision.kv")
        
    def generate_dream(self):
        """generates dream images"""
        dream_description = self.root.dream_description.text
        dream_title = self.root.dream_title.text
        if dream_description != "" and dream_title != "":
            image_data = create_image(dream_description)
            self.save_data = save_image(image_data, 'generated', dream_title)
            sql_functions.save_image(self.connection, dream_title, dream_description, date.today(), 'generated')
        self.load_main_image()

    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        # date_dialog.bind(on_save=self.on_save)
        # date_dialog.open()

    def load_main_image(self):
        """function to load one image"""
        cursor = self.connection.cursor()
        cursor.execute(
            """SELECT file_name FROM dreams
            ORDER BY id DESC
            LIMIT 1;""")
        results = cursor.fetchall()
        if not results:
            self.root.main_image.source = 'images/dream_icon.jpg'
        else:
            self.root.main_image.source = results[0][0]

    def load_gallery(self):
        """function to generate the images in the gallery at launch of the screen"""
        # delete pre-existing widgets
        self.root.ids['gallery'].clear_widgets()
        #obtain list of images
        dreams = sql_functions.read_table(self.connection)
        # generates image line items
        for id, title, description, date, file_name in dreams:
            self.root.ids['gallery'].add_widget(
                Gallery_entry(text=title, 
                secondary_text = description + '\n' + date,
                image_source = file_name,
                icon = 'delete'
                )
            )

    def close_connection(self):
        self.connection.close()
        


# sql_functions.read_table(connection)
dreamvision = Main()
dreamvision.run()
#sql_functions.save_image(dreamvision.connection, 'buongiorno', 'image of coffee', '2023-01-01', 'generated')

# drop_input = input("Do you want to drop the table?")
# if drop_input.lower() == 'y':
#     sql_functions.drop_table(dreamvision.connection)

dreamvision.close_connection()



