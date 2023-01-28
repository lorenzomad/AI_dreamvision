from craiyon import Craiyon

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
 

class Content(MDBoxLayout):
    pass

class Main(MDApp):
    """class that runs the dreamvision.kv file to visualize the frontend"""
    
    dream_text = None
    dream_text = StringProperty(None)

    dialog = None

    def build(self):
        return Builder.load_file("dreamvision.kv")

    def generate_dream(self):
        """generates dream images"""
        
        if self.root.dream_text.text != None:
            
            print("image generation started!\n dream used: " + self.root.dream_text.text )
            generator = Craiyon()
            result = generator.generate(self.root.dream_text.text)
            result.save_images()
            print("images generated")
            return result
        

dreamvision = Main()
dreamvision.run()


    