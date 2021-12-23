from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import date
from texts import *


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.day, self.month, self.year = self.get_date()

        self.outside = GridLayout()
        self.outside.cols = 1

        self.outside.add_widget(Label(text=f'Welcome to year {self.year} advent cat calendar', size_hint_y=None, height=100, font_size=25))

        self.inside = GridLayout()
        self.inside.cols = 7

        for n in range(24):
            my_button1 = Button(text=f"Day {n+1}")
            my_button1.value = n +1
            my_button1.bind(on_release=self.changer)
            if self.month != 12 or n+1 <= self.day:
                self.inside.add_widget(my_button1)
                self.ids[n] = my_button1
            else:
                self.inside.add_widget(Label(text=f"Day {n+1}"))

        self.outside.add_widget(self.inside)
        self.add_widget(self.outside)


    def changer(self, button, *args):
        self.manager.get_screen('second').ids['picture'].source = str(button.value) + '.jpg'
        self.manager.get_screen('second').ids['txt'].text = texts[button.value]
        self.manager.current = 'second'
        self.manager.transition.direction = 'left'

    def get_date(self):
        today = date.today()
        day = today.strftime('%d')
        month = today.strftime('%m')
        year = today.strftime('%Y')

        return int(day), int(month), int(year)


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        self.grid = GridLayout()
        self.grid.cols = 1

        picture = Image(source=f'0')
        label = Label(text='Error', size_hint_y=None, height=100, font_size=15)
        self.grid.add_widget(label)
        self.grid.add_widget(picture)
        self.ids['picture'] = picture
        self.ids['txt'] = label

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