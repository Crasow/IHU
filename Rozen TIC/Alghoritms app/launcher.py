from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from random import randint
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup

from encoder import ShannonFano, LZW, Huffman, ShannonFanoWithConsolidatedAlph, Arithmetic, Hamming, ASCII

# Global settings
Window.size = (900, 500)
# Window.clearcolor = (139 / 255, 0 / 255, 255 / 255, 1) # original
Window.clearcolor = (30 / 255, 2 / 255, 30 / 255, 1)  # baklazhan
# Window.clearcolor = (95 / 255, 50 / 255, 75 / 255, 1) # pink
Window.title = "Binarium"


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.program_name = Label(text='Binarium', font_size=60, italic=True)
        self.input_data = TextInput(hint_text='Введите букву, слово или предложение', multiline=False)
        self.done_status = True

        # self.input_data.bind(text=self.on_text)

    def ascii_button(self, instance):
        ascii_label = Label(text ='Ваш код:\nВаш более читаемый код')
        ascii_res = ASCII(self.input_data.text).code_output()
        ascii_label.text = f'Ваш код: {ascii_res[0]}\n' \
                           f'Ваш более читаемый код: {ascii_res[1]}\n' \
                           f'Длина кода: {len(ascii_res[0])}'

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(ascii_label)
        content.add_widget(close_btn)
        popup = Popup(title='Алгоритм Хаффмана', content=content, auto_dismiss=True, size_hint=[.90, .90])
        popup.open()


    def huffman_button(self, instance):
        huff_label = Label(text='Ваш код:\nВаш более читаемый код:\nВаш словарь: ')
        huff_obj = Huffman(self.input_data.text)
        huff_res = huff_obj.code_output()
        huff_label.text = f'Ваш код: {huff_res[0]}\n' \
                          f'Ваш более читаемый код: {huff_res[1]}\n' \
                          f'Длина кода: {len(huff_res[0])}\n' \
                          f'Ваш словарь: {str(huff_res[2])}'

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(huff_label)
        content.add_widget(close_btn)

        popup = Popup(title='Алгоритм Хаффмана', content=content, auto_dismiss=True, size_hint=[.90, .90])
        popup.open()

    def shafe_button(self, instance):
        shafe_label = Label(text='Ваш код:\nВаш более читаемый код:\nВаш словарь:',
                            size_hint=[.85, .85])
        shafe_obj = ShannonFano(self.input_data.text)
        shafe_res = shafe_obj.code_output()
        shafe_label.text = f'Ваш код: {shafe_res[0].replace(" ", "")}\n' \
                           f'Ваш более читаемый код: {shafe_res[0]}\n' \
                           f'Длина кода: {len(shafe_res[0].replace(" ", ""))}\n' \
                           f'Ваш словарь: {str(shafe_res[1])}'

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(shafe_label)
        content.add_widget(close_btn)

        popup = Popup(title='Алгоритм Шеннон-Фано', content=content, auto_dismiss=True, size_hint=[.90, .90])
        popup.open()

    def shafe_with_cons_button(self, instance):
        shafe_label = Label(text='Ваш код:\nВаш более читаемый код:\nВаш словарь:',
                            size_hint=[.85, .85])
        shafe_obj = ShannonFanoWithConsolidatedAlph(self.input_data.text)
        shafe_res = shafe_obj.code_output()
        shafe_label = Label(text=f'Ваш код: {shafe_res[0].replace(" ", "")}\n' \
                                 f'Ваш более читаемый код: {shafe_res[0]}\n' \
                                 f'Длина кода: {len(shafe_res[0].replace(" ", ""))}\n' \
            # f'Ваш словарь: {str(shafe_res[1])}' \
                                 f'')

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(shafe_label)
        content.add_widget(close_btn)

        popup = Popup(title='Алгоритм Шеннон-Фано с укрупнения алфавита', content=content, auto_dismiss=True,
                      size_hint=[.90, .90])
        popup.open()

    def lzw_button(self, instance):
        class_object = LZW(self.input_data.text)
        results = class_object.code_output()

        def calc_len(code):
            res = 0
            for el in code:
                res += len(el)
            return res

        label = Label(text=f'Ваш код: {results[0]}\n' \
                           f'Длина кода, если кодировать цифры в 8бит: {calc_len(results[0]) * 8}\n' \
            # f'Ваш словарь: {str(results[1])}'
                           f'',
                      size_hint=[.85, .85],
                      halign='left')

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(label)
        content.add_widget(close_btn)

        popup = Popup(title='Алгоритм Лемпеля — Зива — Велча', content=content, auto_dismiss=True, size_hint=[.90, .90])
        popup.open()

    def arithmetic_button(self, instance):
        class_object = Arithmetic(self.input_data.text)
        results = class_object.code_output()

        label = Label(text=f'Закодированная информация находится промежутке\n'
                           f' от {results[0]}\n' \
                           f' до {results[1]}\n',
                      size_hint=[.85, .85],
                      halign='left')

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(label)
        content.add_widget(close_btn)

        popup = Popup(title='Арифметический алгоритм', content=content, auto_dismiss=True, size_hint=[.90, .90])
        popup.open()

    def hamming_button(self, instance):
        class_obj = Hamming(self.input_data.text)
        encoded = class_obj.encode()
        encoded_with_error = class_obj.set_errors(encoded)
        decoded_wth_mistakes = class_obj.decode(encoded_with_error, fix_errors=False)
        right_decoded = class_obj.decode(encoded_with_error)
        label = Label(text=f'Длина блока кодирования: {class_obj.CHUNK_LENGTH}\n'
                           f'Контрольные биты: {class_obj.CHECK_BITS}\n'
        # f'Закодированные данные: {encoded}\n'
                           f'Результат декодирования: {class_obj.decode(encoded)}\n'
        # f'Допускаем ошибки в закодированных данных: {class_obj.set_errors(encoded)}\n'
                           f'Допущены ошибки в битах: {class_obj.get_diff_index_list(encoded, encoded_with_error)}\n'
                           f'Результат декодирования ошибочных данных без исправления ошибок: {decoded_wth_mistakes}\n'
                           f'Результат декодирования ошибочных данных с исправлением ошибок: {right_decoded}\n',
                      size_hint=[.85, .85],
                      halign='left')

        content = BoxLayout()
        close_btn = Button(text="Close", size_hint=[.15, .15])

        content.add_widget(label)
        content.add_widget(close_btn)

        popup = Popup(title='Алгоритм Хамминга', content=content, auto_dismiss=True, size_hint=[.90, .90])
        popup.open()

    def build(self):
        top_left_box = BoxLayout(size_hint=[.5, .5], padding=[25, 65, 25, 75])
        top_left_box.add_widget(self.input_data)

        top_right_box = BoxLayout(size_hint=[.33, .18])
        top_right_box.add_widget(self.program_name)

        bottom_grid = GridLayout(cols=4, size_hint=[1, .5], padding=25, spacing=30)
        bottom_grid.add_widget(Button(text='ASCII', on_press = self.ascii_button))
        bottom_grid.add_widget(Button(text='Шеннон-Фано', on_press=self.shafe_button))
        bottom_grid.add_widget(Button(text='Хаффман', on_press=self.huffman_button))
        bottom_grid.add_widget(Button(text='Шеннон-Фано с УА', on_press=self.shafe_with_cons_button))
        bottom_grid.add_widget(Button(text='LZW', on_press=self.lzw_button))
        bottom_grid.add_widget(Button(text='Арифметический', on_press=self.arithmetic_button))
        bottom_grid.add_widget(Button(text='Хамминг', on_press=self.hamming_button))
        bottom_grid.add_widget(Button(text='X'))

        top_left_anchor = AnchorLayout(anchor_x='left', anchor_y='top')
        top_left_anchor.add_widget(top_left_box)

        top_right_anchor = AnchorLayout(anchor_x='right', anchor_y='top')
        top_right_anchor.add_widget(top_right_box)

        bottom_anchor = AnchorLayout(anchor_y='bottom')
        bottom_anchor.add_widget(bottom_grid)

        main_anchor = AnchorLayout()
        main_anchor.add_widget(bottom_anchor)
        main_anchor.add_widget(top_right_anchor)
        main_anchor.add_widget(top_left_anchor)

        return main_anchor

# ASCII
# BCH
# Turbo code
# Convolution

if __name__ == "__main__":
    MyApp().run()
