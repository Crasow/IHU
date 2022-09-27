from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from random import randint
from kivy.core.window import Window

# Global settings
Window.size = (900, 500)
Window.clearcolor = (139 / 255, 0 / 255, 255 / 255, 1)
Window.title = "Бинариум"


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Бинариум')
        self.sf = Label(text = 'Шаннон-Фено')
        self.code = Label(text='Ваш код')
        self.dict = Label(text='Ваш словарь')
        self.input_data = TextInput(hint_text='Введите букву, слово или предложение', multiline=False)
        self.input_data.bind (text = self.on_text)

    def on_text(self, *args):
        data = self.input_data.text


    def build(self):
        box = BoxLayout()
        box.add_widget(self.label)
        box.add_widget(button)

        return box


if __name__ == "__main__":
    MyApp().run()
