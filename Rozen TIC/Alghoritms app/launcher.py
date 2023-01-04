from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from random import randint
from kivy.core.window import Window

from encoder import ShannonFano
from encoder import Huffman

# Global settings
Window.size = (900, 500)
Window.clearcolor = (139 / 255, 0 / 255, 255 / 255, 1)
Window.title = "Бинариум"


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Бинариум')
        self.input_data = TextInput(hint_text='Введите букву, слово или предложение', multiline=False)
        self.shafe = Label(text='Алгоритм Шаннон-Фено\nВаш код:\nВаш более читаемый код:\nВаш словарь: ')
        self.huff = Label(text='Алгоритм Хаффмана\nВаш код:\nВаш более читаемый код:\nВаш словарь: ')
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        user_data = self.input_data.text
        if user_data:
            shafe_obj = ShannonFano(user_data)
            shafe_res = shafe_obj.code_output()
            self.shafe.text = f'Алгоритм Шаннон-Фено\n ' \
                              f'Ваш код: {shafe_res[0].replace(" ", "")}\n ' \
                              f'Ваш более читаемый код:{shafe_res[0]}\n ' \
                              f'Длина кода:{len(shafe_res[0].replace(" ", ""))}\n ' \
                              f'Ваш словарь: {str(shafe_res[1])} '

            huff_obj = Huffman(user_data)
            huff_res = huff_obj.code_output()
            self.huff.text = f'Алгоритм Хаффмана\n ' \
                             f'Ваш код: {huff_res[0]}\n ' \
                             f'Ваш более читаемый код:{huff_res[1]}\n ' \
                             f'Длина кода:{len(huff_res[0])}\n ' \
                             f'Ваш словарь: {str(huff_res[2])} '



    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.shafe)
        box.add_widget(self.huff)

        return box


if __name__ == "__main__":
    MyApp().run()
