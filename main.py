from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import date


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.outside = GridLayout()
        self.outside.cols = 1

        self.outside.add_widget(Label(text='Hello', size_hint_y=None, height=100, font_size=25))

        self.inside = GridLayout()
        self.inside.cols = 7

        for n in range(24):
            my_button1 = Button(text=f"Day {n+1}")
            my_button1.bind(on_release=self.changer)
            self.inside.add_widget(my_button1)

        self.outside.add_widget(self.inside)
        self.add_widget(self.outside)


    def changer(self, *args):
        self.manager.current = 'second'
        self.manager.transition.direction = 'left'

    def get_date(self):
        pass


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        self.grid = GridLayout()
        self.grid.cols = 1

        self.grid.add_widget(Image(source='1.jpg'))

        button = Button(text="To main page", size_hint_y=None, height=100, font_size=25)
        button.bind(on_release=self.changer)
        self.grid.add_widget(button)

        self.add_widget(self.grid)

    def changer(self, *args):
        self.manager.current = 'main'
        self.manager.transition.direction = 'right'



class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        screen1 = MainWindow(name='main')
        screen2 = SecondWindow(name='second')
        self.add_widget(screen1)
        self.add_widget(screen2)



class MyApp(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    MyApp().run()