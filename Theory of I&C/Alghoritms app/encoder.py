from collections import Counter


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
    def __init__(self, user_data, bits_in_file):
        self.dictionary = []
        self.user_data = user_data
        self.maximum_table_size = pow(2, int(bits_in_file))

    def create_dict(self):
        self.dictionary = [chr(i) for i in range(256)]
        # unic_symbols = set(self.user_data)
        # for el in unic_symbols:
        #     self.dictionary.append(el)

    def code_output(self):
        self.create_dict()
        new_str = ''
        code = []
        cnt = 0
        is_full = 0
        for char in self.user_data:
            if cnt % 100000 == 0 and cnt != 0:
                print(f'{cnt} cycles gone')
            cnt += 1
            if new_str + char in self.dictionary:
                new_str += char
            else:
                code.append(self.dictionary.index(new_str))
                if len(self.dictionary) < 1000:
                    self.dictionary.append(new_str + char)
                elif is_full == 0 and len(self.dictionary) >= 1000:  # 500 = 2275375 1000 = 2417320 15000 = 2609497
                    print(f'Dictionary have been fulled on {cnt} cycle')
                    is_full = 1
                new_str = char
        if new_str:
            code += str(self.dictionary.index(new_str))
        return code


if __name__ == '__main__':
    def shan_test(big_text_factor=1, big_or_small=0):
        print('-' * 50)

        def test(text):
            a = ShannonFano(text).code_output()
            b = ShannonFanoWithConsolidatedAlph(text).code_output()
            return a, b

        if big_or_small == 0:
            test_text = '322.4 В случае двоичного источника без памяти, когда знаки разновероятные, энтропия меньше 1 дв.ед. (рис. 1). Например, P(a1) = 0,8 , P(a2) = 0,2. Тогда энтропия равна H(A) = 0,722 дв.ед. Применение эффективного кодирования (например, кода Хаффмана) к такому двоичному источнику не даст никакого эффекта (каждый из знаков будет кодироваться одним двоичным символом, независимо от вероятности его появления). Для эффективного кодирования нужное предварительное укрупнение алфавита. Под укрупнением алфавита будем понимать формирование нового алфавита укрупненных знаков (укрупненный знак является соединением из m знаков первичного алфавита). Объем нового (вторичного) алфавита MB определяется как'
            test_text *= big_text_factor
        else:
            test_text = 'arrrre'

        print(f'Length of string for Shannon algs: {len(test_text)}')
        small_text = 'arrrre'

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


    # first arg - int, by which big text is multipled # default = 1
    # second arg - bool, big(0) or small(1) text to use # default = 0
    shan_test()

    huff_test()
