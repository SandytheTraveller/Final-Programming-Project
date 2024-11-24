from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from menu_screen import MenuScreen
from hallOfFame import HallOfFame

Builder.load_file('cannon.kv')


class MyScreenManager(ScreenManager):
    pass


class CannonApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    CannonApp().run()

