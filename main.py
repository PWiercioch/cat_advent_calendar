from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from datetime import date


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.test_text = 'test'

        self.inside = GridLayout()
        self.inside.cols = 2

        my_button1 = Button(text="Go to screen 1")
        my_button1.bind(on_release=self.changer)
        self.inside.add_widget(my_button1)

        self.add_widget(self.inside)

        # self.add_widget(Label(text="Hello"))
        # self.ids["loki"].text = "loki: >_<!!!"

        '''
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Hello"))

        for n in range(25):
            print(n)
            # self.inside.add_widget(Label(text=f"Hello nr:{n}"))
            # self.inside.add_widget(Image(source=self.get_date()))

        self.add_widget(self.inside)

        self.inside.add_widget(Button(text="To second page", font_size=40))
        '''

    def changer(self ,*args):
        self.manager.current = 'second'

    def add_content(self):
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Hello"))
        self.inside.add_widget(Label(text="Hello"))

    def get_date(self):
        data = date.today()
        if int(data.strftime("%d")) == 5:
            return '1.jpg'
        else:
            return '2.jpg'


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        '''
        self.cols = 1

        self.add_widget(Button(text="To main page", font_size=40))
        '''


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        screen1 = MainWindow(name='main')
        screen2 = SecondWindow(name='second')
        self.add_widget(screen1)
        self.add_widget(screen2)


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    MyApp().run()