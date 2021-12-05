import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from datetime import date


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Button(text="Submit", font_size=40))

        for n in range(25):
            print(n)
            # self.inside.add_widget(Label(text=f"Hello nr:{n}"))
            # self.inside.add_widget(Image(source=self.get_date()))

        self.add_widget(self.inside)

        self.add_widget(Button(text="Submit", font_size=40))

    def get_date(self):
        data = date.today()
        if int(data.strftime("%d")) == 5:
            return '1.jpg'
        else:
            return '2.jpg'



class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()