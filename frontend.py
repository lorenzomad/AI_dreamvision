import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

import main


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):

        self.random_label.text = str(random.randint(1,10))

class DreamVision(App):

    def build(self):
        return MyRoot()

dreamvision = DreamVision()
dreamvision.run()