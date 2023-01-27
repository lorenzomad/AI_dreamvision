from craiyon import Craiyon

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
 

class Content(MDBoxLayout):
    pass

class Main(MDApp):
    """class that runs the dreamvision.kv file to visualize the frontend"""
    
    dream_text = ObjectProperty(None)

    data = {
        'Add dream': 'pencil'
    }

    dialog = None

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
        
    def show_dream_popup(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Add dream",
                type="custom",
                content_cls= Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

dreamvision = Main()
dreamvision.run()


    