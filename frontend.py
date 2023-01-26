#import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder

#from kivy.uix.boxlayout import BoxLayout
import random

import main


class Main(MDApp):

    def build(self):
        return Builder.load_file("dreamvision.kv")

    def generate_number(self):
        label = self.root.ids.random_label
        label.text = str(random.randint(1,10))



dreamvision = Main()
dreamvision.run()