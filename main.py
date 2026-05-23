from kivy.app import App
from kivy.uix.button import Button

class GameApp(App):
    def build(self):
        return Button(text="My Android Game")

GameApp().run()