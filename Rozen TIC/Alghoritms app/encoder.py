from collections import Counter
from decimal import Decimal
import random


class ShannonFano:

    def __init__(self, user_data):
        self.user_data = user_data

        # Creating list of tuples with pairs (symbol, qty in word)
        self.word_counter = sorted(Counter(self.user_data).items())

        # Creating list with lists [symbol, qty in word, space for self.code]
        for indx, el in enumerate(self.word_counter):
            self.word_counter[indx] = list(el) + ['']

        self.code = []  # result [symbol, qty in word, self.code]
        self.code_dict = {}  # comfortable dict {symbol:self.code}
        self.encoded_word = []  # readable self.code

    def calculate_probability(self):
        word_len = len(self.user_data)
        for el in range(len(self.word_counter)):
            self.word_counter[el][1] /= word_len

    def encoding(self, arr):
        # check for empty arr
        if not arr:
            return
        # check for only 1 incoming value
        elif len(arr) == 1:
            arr[0][2] += '0'
            self.code.append(arr)
            return self.encoded_word

        left, right = [], []
        half_indx = 0  # indx of the middle element of the arr
        freq_sum = 0  # Sum of symbol frequencies in the recieved arr

        for el in arr:
            freq_sum += el[1]

        # Find index of middle symbol by frequnce
        summ = 0
        for el in range(len(arr)):
            summ += arr[el][1]
            if summ * 2 >= freq_sum:
                half_indx = el + (abs(2 * summ - freq_sum) < abs(2 * (summ - arr[el][1]) - freq_sum))
                break

        # Main recursive part
        for el in arr[:half_indx]:
            el[2] += '0'  # add 0 for code of all elements in left part
            left.append(el)  # and add to left list for next separation
        for el in arr[half_indx:]:
            el[2] += '1'  # 1 for right part
            right.append(el)  # same to right list

        if len(left) == 1:  # first exit condititon
            # if only 1 el in list, then there is nothing to separate so send to final code
            self.code.append(left)
        else:
            self.encoding(left)  # recursion for left part until there will be only 1 el
        if len(right) == 1:  # second exit condititon
            self.code.append(right)
        else:
            self.encoding(right)

    def code_output(self):
        self.calculate_probability()
        self.encoding(self.word_counter)

        for el in range(len(self.user_data)):
            for c_el in range(len(self.code)):
                if self.user_data[el] == self.code[c_el][0][0]:
                    self.encoded_word.append(self.code[c_el][0][2])
        self.encoded_word = ' '.join(self.encoded_word)

        for el in range(len(self.code)):
            self.code_dict[self.code[el][0][0]] = self.code[el][0][2]

        return self.encoded_word, self.code_dict


class ShannonFanoWithConsolidatedAlph(ShannonFano):

    def alphabet_consolidation(self):
        self.calculate_probability()
        consolidated_alph = []
        joined_cons_alph = []
        cons_alph_freq = []
        # create list of lists of consolidated alph
        for el in self.word_counter:
            for ell in self.word_counter:
                for elll in self.word_counter:
                    consolidated_alph.append([el[0], ell[0], elll[0]])

        # turn list of list into list of strings of consolidated alph
        for el in range(len(consolidated_alph)):
            joined_cons_alph.append(''.join(consolidated_alph[el]))

        for el in joined_cons_alph:
            freq_prod = 1
            for ell in el:
                for i in self.word_counter:
                    if ell == i[0]:
                        freq_prod *= i[1]
            cons_alph_freq.append([el, freq_prod, ''])
        self.word_counter = cons_alph_freq

        return cons_alph_freq

    def code_output(self):
        self.alphabet_consolidation()
        self.encoding(self.word_counter)

        start, stop = 0, 3
        for el in range(0, len(self.user_data), 3):
            user_data_part = self.user_data[start:stop]
            start += 3
            stop += 3
            for ell in range(len(self.code)):
                if user_data_part == self.code[ell][0][0]:
                    self.encoded_word.append(self.code[ell][0][2])
        self.encoded_word = ' '.join(self.encoded_word)

        for el in range(len(self.code)):
            self.code_dict[self.code[el][0][0]] = self.code[el][0][2]

        return self.encoded_word, self.code_dict


class Huffman:
    def __init__(self, user_data):
        self.user_data = user_data  # data to encode
        self.sym_prob = {}  # dict of symbols-probabilities pairs
        self.end_node = None  # end node contains a tree
        self.symbol_codes_dict = {}  # dict of symbol-code pairs

    class Node:
        def __init__(self, symbol, prob, right=None, left=None):
            self.prob = prob
            self.symbol = symbol
            self.left = left
            self.right = right
            self.code = ''

    def calculate_probability(self):
        # create pairs symbol-frequency -> sort them by freq -> turn it to dict
        sym_freq = dict(sorted(Counter(self.user_data).items()))

        # calculate probabilities of symbols and save as dict
        for k in sym_freq.keys():
            self.sym_prob[k] = (sym_freq[k] / len(self.user_data))
        return sym_freq

    def tree_create(self):
        # create list of basic nodes
        nodes = []
        for k, v in self.sym_prob.items():
            nodes.append(self.Node(symbol=k, prob=v))

        # cycle of Huffman coding
        while len(nodes) > 1:
            # sort ascending
            nodes = sorted(nodes, key=lambda x: x.prob)
            # get two node with minimal frequency and delete them from list
            left = nodes.pop(0)
            right = nodes.pop(0)
            # left always get 0 and right always get 1
            left.code = '0'
            right.code = '1'
            # add new node to list
            nodes.append(self.Node(symbol=left.symbol + right.symbol,
                                   prob=left.prob + right.prob,
                                   left=left, right=right))

        self.end_node = nodes[0]

    def encode_symbols(self, node, code=''):
        """Func runs through the tree and assigns code for every basic symbol"""
        symbol_code = code + node.code

        # if node has left or right child - it`s not a basic symbol node
        if node.left:
            self.encode_symbols(node.left, symbol_code)
        if node.right:
            self.encode_symbols(node.right, symbol_code)
        # if it`s basic node - add symbol of node and accumulated code to dict as a pair
        if not node.left and not node.right:
            self.symbol_codes_dict[node.symbol] = symbol_code

    def code_output(self):
        # doing main stuff
        self.calculate_probability()
        self.tree_create()
        self.encode_symbols(self.end_node)

        # if only one symbol entered by user - it always has code '0'
        if len(self.symbol_codes_dict) == 1:
            for key in self.symbol_codes_dict.keys():
                self.symbol_codes_dict[key] = '0'

        # encode user data by created dict
        encoded_data = []
        for el in self.user_data:
            for key in self.symbol_codes_dict.keys():
                if el == key:
                    encoded_data.append(self.symbol_codes_dict[key])
        code = ''.join(encoded_data)
        readable_code = ' '.join(encoded_data)

        # ascending sort by symbol code length
        sorted_codes_dict = {}
        sorted_tuples = sorted(self.symbol_codes_dict.items(), key=lambda item: len(item[1]))
        for el in range(len(sorted_tuples)):
            sorted_codes_dict[sorted_tuples[el][0]] = sorted_tuples[el][1]

        return code, readable_code, sorted_codes_dict


class LZW:
    def __init__(self, user_data):
        self.user_data = user_data

    def create_dict(self):
        dictionary = [chr(i) for i in range(256)]
        dictionary += 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я а б в г д е ё ж з и й к ' \
                      'л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
        return dictionary

    def code_output(self):
        dictionary = self.create_dict()
        string = ''
        compressed_data = []
        cnt = 0
        # is_full = 0
        max_size = pow(2, len(self.user_data))
        for char in self.user_data:

            if cnt % 100000 == 0 and cnt != 0:
                print(f'{cnt} cycles gone')
            cnt += 1

            if string + char in dictionary:
                string += char
            else:
                compressed_data.append(str(dictionary.index(string)))
                if len(dictionary) <= max_size:
                    dictionary.append(string + char)
                # else:
                #     is_full += 1
                string = char

                # if is_full == 1:
                #     print(f'Dictionary have been fulled on {cnt} cycle')

        if string:
            compressed_data.append(str(dictionary.index(string)))
        return compressed_data


class Arithmetic:
    def __init__(self, user_data):
        self.user_data = user_data

    def create_dict(self):
        data = self.user_data
        char_prob_list = []
        char_set = set(data)
        for el in char_set:
            char_prob = self.calculate_char_probability(el)
            char_prob_list.append([el, char_prob])
        return char_prob_list

    def calculate_char_probability(self, char):
        cnt = 0
        data = self.user_data
        for el in range(len(data)):
            if char == data[el]:
                cnt += 1
        return cnt / len(data)

    def coding(self):
        char_prob = sorted(self.create_dict(), key=lambda x: x[1], reverse=True)
        left, right = Decimal('0'), Decimal('1')

        for letter in self.user_data:
            cnt = 0

            for el in char_prob:
                if letter in el:
                    break
                cnt += 1

            letter_indx = cnt
            left_sum, right_sum = Decimal('0'), Decimal('0')

            for el in range(0, letter_indx):
                left_sum += Decimal(char_prob[el][1])

            for el in range(0, letter_indx + 1):
                right_sum += Decimal(char_prob[el][1])

            left, right = (left + (right - left) * left_sum,
                           left + (right - left) * right_sum)

        return left, right


class Hamming:
    def __init__(self, user_data):
        self.user_data = user_data
        self.CHUNK_LENGTH = 8
        assert not self.CHUNK_LENGTH % 8, 'Длина блока должна быть кратна 8'     # проверка длины блока
        self.CHECK_BITS = [i for i in range(1, self.CHUNK_LENGTH + 1) if not i & (i - 1)]     # вычисление контрольных бит





    def chars_to_bin(self, chars):
        """
        Преобразование символов в бинарный формат
        """
        arr = []
        assert not len(chars) * 8 % self.CHUNK_LENGTH, 'Длина кодируемых данных должна быть кратна длине блока кодирования'
        res = ''.join([bin(ord(c))[2:].zfill(8) for c in chars])
        for c in chars:

            arr.append( bin(ord(c))[2:].zfill(8) )
        return res

    def chunk_iterator(self, text_bin, chunk_size=None):
        if not chunk_size:
            chunk_size = self.CHUNK_LENGTH
        """
        Поблочный вывод бинарных данных
        """
        for i in range(len(text_bin)):
            if not i % chunk_size:
                yield text_bin[i:i + chunk_size]

    def get_check_bits_data(self, value_bin):
        """
        Получение информации о контрольных битах из бинарного блока данных
        """
        check_bits_count_map = {k: 0 for k in self.CHECK_BITS}
        for index, value in enumerate(value_bin, 1):
            if int(value):
                bin_char_list = list(bin(index)[2:].zfill(8))
                bin_char_list.reverse()
                for degree in [2 ** int(i) for i, value in enumerate(bin_char_list) if int(value)]:
                    check_bits_count_map[degree] += 1
        check_bits_value_map = {}
        for check_bit, count in check_bits_count_map.items():
            check_bits_value_map[check_bit] = 0 if not count % 2 else 1
        return check_bits_value_map

    def set_empty_check_bits(self, value_bin):
        """
        Добавить в бинарный блок "пустые" контрольные биты
        """
        for bit in self.CHECK_BITS:
            value_bin = value_bin[:bit - 1] + '0' + value_bin[bit - 1:]
        return value_bin

    def set_check_bits(self, value_bin):
        """
        Установить значения контрольных бит
        """
        value_bin = self.set_empty_check_bits(value_bin)
        check_bits_data = self.get_check_bits_data(value_bin)
        for check_bit, bit_value in check_bits_data.items():
            value_bin = '{0}{1}{2}'.format(
                value_bin[:check_bit - 1], bit_value, value_bin[check_bit:])
        return value_bin

    def get_check_bits(self, value_bin):
        """
        Получить информацию о контрольных битах из блока бинарных данных
        """
        check_bits = {}
        for index, value in enumerate(value_bin, 1):
            if index in self.CHECK_BITS:
                check_bits[index] = int(value)
        return check_bits

    def exclude_check_bits(self, value_bin):
        """
        Исключить информацию о контрольных битах из блока бинарных данных
        """
        clean_value_bin = ''
        for index, char_bin in enumerate(list(value_bin), 1):
            if index not in self.CHECK_BITS:
                clean_value_bin += char_bin

        return clean_value_bin

    def set_errors(self, encoded):
        """
        Допустить ошибку в блоках бинарных данных
        """
        result = ''
        for chunk in self.chunk_iterator(encoded, self.CHUNK_LENGTH + len(self.CHECK_BITS)):
            num_bit = random.randint(1, len(chunk))
            chunk = '{0}{1}{2}'.format(chunk[:num_bit - 1], int(chunk[num_bit - 1]) ^ 1, chunk[num_bit:])
            result += (chunk)
        return result

    def check_and_fix_error(self, encoded_chunk):
        """
        Проверка и исправление ошибки в блоке бинарных данных
        """
        check_bits_encoded = self.get_check_bits(encoded_chunk)
        check_item = self.exclude_check_bits(encoded_chunk)
        check_item = self.set_check_bits(check_item)
        check_bits = self.get_check_bits(check_item)
        if check_bits_encoded != check_bits:
            invalid_bits = []
            for check_bit_encoded, value in check_bits_encoded.items():
                if check_bits[check_bit_encoded] != value:
                    invalid_bits.append(check_bit_encoded)
            num_bit = sum(invalid_bits)
            encoded_chunk = '{0}{1}{2}'.format(
                encoded_chunk[:num_bit - 1],
                int(encoded_chunk[num_bit - 1]) ^ 1,
                encoded_chunk[num_bit:])
        return encoded_chunk

    def get_diff_index_list(self, value_bin1, value_bin2):
        """
        Получить список индексов различающихся битов
        """
        diff_index_list = []
        for index, char_bin_items in enumerate(zip(list(value_bin1), list(value_bin2)), 1):
            if char_bin_items[0] != char_bin_items[1]:
                diff_index_list.append(index)
        return diff_index_list

    def encode(self):
        source = self.user_data
        """
        Кодирование данных
        """
        text_bin = self.chars_to_bin(source)
        result = ''
        for chunk_bin in self.chunk_iterator(text_bin):
            chunk_bin = self.set_check_bits(chunk_bin)
            result += chunk_bin
        return result

    def decode(self, encoded, fix_errors=True):
        """
        Декодирование данных
        """
        decoded_value = ''
        fixed_encoded_list = []
        for encoded_chunk in self.chunk_iterator(encoded, self.CHUNK_LENGTH + len(self.CHECK_BITS)):
            if fix_errors:
                encoded_chunk = self.check_and_fix_error(encoded_chunk)
            fixed_encoded_list.append(encoded_chunk)

        clean_chunk_list = []
        for encoded_chunk in fixed_encoded_list:
            encoded_chunk = self.exclude_check_bits(encoded_chunk)
            clean_chunk_list.append(encoded_chunk)

        for clean_chunk in clean_chunk_list:
            for clean_char in [clean_chunk[i:i + 8] for i in range(len(clean_chunk)) if not i % 8]:
                decoded_value += chr(int(clean_char, 2))
        return decoded_value


if __name__ == '__main__':
    def create_data(big_text_factor=1, big_or_small_val=0):
        if big_or_small_val == 0:
            # test_text = '322.4 В случае двоичного источника без памяти, когда знаки разновероятные, энтропия меньше ' \
            #             '1 дв.ед. (рис. 1). Например, P(a1) = 0,8 , P(a2) = 0,2. Тогда энтропия равна H(A) = 0,' \
            #             '722 дв.ед. Применение эффективного кодирования (например, кода Хаффмана) к такому двоичному ' \
            #             'источнику не даст никакого эффекта (каждый из знаков будет кодироваться одним двоичным ' \
            #             'символом, независимо от вероятности его появления). Для эффективного кодирования нужное ' \
            #             'предварительное укрупнение алфавита. Под укрупнением алфавита будем понимать формирование ' \
            #             'нового алфавита укрупненных знаков (укрупненный знак является соединением из m знаков ' \
            #             'первичного алфавита). Объем нового (вторичного) алфавита MB определяется как '
            # test_text *= big_text_factor
            test_text = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a ' \
                            'piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard ' \
                            'McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of ' \
                            'the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through ' \
                            'the cites of the word in classical literature, discovered the undoubtable source. Lorem ' \
                            'Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The ' \
                            'Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the ' \
                            'theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, ' \
                            '"Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. '
        else:
            test_text = 'arrrre'
        return test_text


    # (<how many times the text is enlarged>,<1 - small, 0 - big>)
    def shan_test(big_text_factor=1, big_or_small_val=0):
        print('-' * 50)

        test_text = create_data(big_text_factor, big_or_small_val)

        def test(text):
            a = ShannonFano(text).code_output()
            b = ShannonFanoWithConsolidatedAlph(text).code_output()
            return a, b

        print(f'Length of string for Shannon algs: {len(test_text)}')

        ShannonFannoObj, ShannonFanoConsObj = test(test_text)
        # print(ShannonFannoObj[0])
        shannon_len = len(ShannonFannoObj[0].replace(' ', ''))
        print(f'Casual code length:  {shannon_len}')

        # print(ShannonFanoConsObj[0])
        cons_shano_len = len(ShannonFanoConsObj[0].replace(' ', ''))
        print(f'With consolidated alph code length:  {cons_shano_len}')
        print(f'Cons code efficiency: {1 - (cons_shano_len / shannon_len)}')
        print('-' * 50)


    def huff_test():
        print('-' * 50)
        string = 'телефонеон'
        print(f'Length of strring for Huffman: {len(string)}')
        print(f'Code: {Huffman(string).code_output()[0]}')
        print(f'Readable code: {Huffman(string).code_output()[1]}')
        print(f'Dict: {Huffman(string).code_output()[2]}')
        print('-' * 50)


    def lzw_test(big_text_factor=1, big_or_not=0):
        data = create_data(big_text_factor, big_or_not)
        var = LZW(data)

        a = var.code_output()
        print(f'Результат: \n{a} ')
        a = ''.join(a)
        print('-' * 30)
        print(f'{len(data)} - длина исходного текста')
        print(f'{len(a)} - длина последовательности чисел кодированого исходного текста')


    def ariphmetic_test():
        data = 'abacaba'
        var = Arithmetic(data)
        # print(f'{len(data)}')
        res = var.coding()
        print(f'{res[0]}')
        print(f'{res[1]}')


    def hamming_test(big_or_small):
        print('-'*50)
        hamm_obj = Hamming(create_data(big_or_small_val=big_or_small))
        print('Длина блока кодирования: {0}'.format(hamm_obj.CHUNK_LENGTH))
        print('Контрольные биты: {0}'.format(hamm_obj.CHECK_BITS))
        encoded = hamm_obj.encode()
        print('Закодированные данные: {0}'.format(encoded))
        decoded = hamm_obj.decode(encoded)
        print('Результат декодирования: {0}'.format(decoded))
        encoded_with_error = hamm_obj.set_errors(encoded)
        print('Допускаем ошибки в закодированных данных: {0}'.format(encoded_with_error))
        diff_index_list = hamm_obj.get_diff_index_list(encoded, encoded_with_error)
        print('Допущены ошибки в битах: {0}'.format(diff_index_list))
        decoded = hamm_obj.decode(encoded_with_error, fix_errors=False)
        print('Результат декодирования ошибочных данных без исправления ошибок: {0}'.format(decoded))
        decoded = hamm_obj.decode(encoded_with_error)
        print('Результат декодирования ошибочных данных с исправлением ошибок: {0}'.format(decoded))


    # first arg - int, by which big text is multipled # default = 1
    # second arg - bool, big(0) or small(1) text to use # default = 0
    # lzw_test(big_text_factor=100)
    # shan_test()
    # huff_test()

    # ariphmetic_test()

    hamming_test(0)
