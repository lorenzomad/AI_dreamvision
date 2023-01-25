import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label


class DreamVision(App):

    def build(self):
        return Label(text="DreamVision")

dreamvision = DreamVision()
dreamvision.run()