import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

Config.set('graphics', 'width', '360') 
Config.set('graphics', 'height', '620')
Config.set('graphics', 'resizable', '0') 


class MainApp(App):

    def build(self):
        return MainGrid()


    def on_pause(self):
        print("App paused.")
        return True 


    def on_resume(self):
        print("App resumed.")


class MainGrid(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def minimize(self):
        App.get_running_app().stop()
        Clock.schedule_once(self.resume_app, 5)


    def resume_app(self, dt):
        print("Reopening app...")
        App.get_running_app().run()


    def update_zoom(self, value):
        if value == '+':
            self.minimize()
        elif value == '-':
            self.minimize()


if __name__ == '__main__':
    MainApp().run()