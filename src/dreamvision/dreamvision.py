"""dreamvision file with frontend interface
and supporting functions"""
#general imports
import os
import base64
import sqlite3
from datetime import date

#craiyon library import
from craiyon import Craiyon

#kivy imports
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.properties import StringProperty

#local imports
import sql_functions

def create_image(prompt):
    """generates image from the defined prompt using craiyon"""
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
    while os.path.exists(file_name):
        file_name = file_name.replace('.jpg', '(1).jpg')
    #write image file to disk
    with open(file_name, 'wb') as file:
        file.write(image_data)

def load_last_image(connection):
    """function to load the latest image"""
    cursor = connection.cursor()
    cursor.execute(
        """SELECT file_name FROM dreams
        ORDER BY id DESC
        LIMIT 1;""")
    results = cursor.fetchall()
    if not results:
        return 'images/dream_icon.jpg'
    return results[0][0]

class Gallery_entry(TwoLineAvatarIconListItem):
    """kv custom object to visualize one dream entry in the dream gallery"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    image_source = StringProperty("")


class Dreamvision(MDApp):
    """Kivy class for the frontend: 
    loads the main interface of the app"""
    #connect db
    connection = sqlite3.connect("dreams.db")
    sql_functions.create_db(connection)

    def build(self):
        return Builder.load_file("dreamvision.kv")

    def on_start(self, **kwargs):
        """on start let's load the latest image generated"""
        self.load_main_image()

    def generate_dream(self):
        """generates dream images"""
        dream_description = self.root.dream_description.text
        dream_title = self.root.dream_title.text
        if dream_description != "" and dream_title != "":
            image_data = create_image(dream_description)
            save_image(image_data, 'generated', dream_title)
            sql_functions.save_image(self.connection, 
                                     dream_title, 
                                     dream_description, 
                                     date.today(), 
                                     'generated'
                                    )
        self.load_main_image()

    def load_main_image(self):
        """loads the last image available"""
        self.root.main_image.source = load_last_image(self.connection) 

    def remove_image(self, filepath):
        """removes the image from the db and the memory (if exists)"""
        sql_functions.delete_image(self.connection, filepath)
        if os.path.exists(filepath):
            os.remove(filepath)
        self.load_gallery()

    def load_gallery(self):
        """function to generate the images in the gallery at launch of the screen"""
        # delete pre-existing widgets to avoid duplicates
        self.root.ids['gallery'].clear_widgets()
        #obtain list of images
        dreams = sql_functions.read_table(self.connection)
        # generates image line items
        for id, title, description, date, file_name in dreams:
            self.root.ids['gallery'].add_widget(
                Gallery_entry(text=title, 
                secondary_text = description + '\n' + date,
                image_source = file_name
                )
            )

    def close_connection(self):
        """closes the connection to the server"""
        self.connection.close()
