from collections import Counter


class ShannonFano:

    def __init__(self, user_word):
        self.user_word = user_word

        # Creating list of tuples with pairs (symbol, qty in word)
        self.word_counter = sorted(Counter(self.user_word).items())

        # Creating list with lists [symbol, qty in word, space for self.code]
        for indx, el in enumerate(self.word_counter):
            self.word_counter[indx] = list(el) + ['']

        self.code = []  # result [symbol, qty in word, self.code]
        self.code_dict = {}  # comfortable dict {symbol:self.code}
        self.encoded_word = []  # readable self.code

    def calculate_probability(self):
        word_len = len(self.user_word)
        for el in range(len(self.word_counter)):
            self.word_counter[el][1] = self.word_counter[el][1] / word_len

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

        for i, el in enumerate(arr):
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

    def get_code(self):
        self.calculate_probability()
        self.encoding(self.word_counter)

        for el in range(len(self.user_word)):
            for c_el in range(len(self.code)):
                if self.user_word[el] == self.code[c_el][0][0]:
                    self.encoded_word.append(self.code[c_el][0][2])
        self.encoded_word = ' '.join(self.encoded_word)

        for el in range(len(self.code)):
            self.code_dict[self.code[el][0][0]] = self.code[el][0][2]

        return self.encoded_word, self.code_dict


class Huffman(ShannonFano):
    def __init__(self, user_word):
        super().__init__(user_word)

    class Node:
        def __init__(self, prob, symbol, left=None, right=None):
            self.prob = prob
            self.symbol = symbol
            self.left = left
            self.right = right
            self.code = ''

    def calculate_probability(self):
        symbols = dict()
        for element in self.user_word:
            if symbols.get(element) is None:
                symbols[element] = 1
            else:
                symbols[element] += 1
        return symbols

    codes = dict()

    def calculate_codes(self, node, val=''):
        new_val = val + str(node.code)

        if node.left:  # remove brackets
            self.calculate_codes(node.left, new_val)
        if node.right:  # remove brackets
            self.calculate_codes(node.right, new_val)

        if not node.left and not node.right:
            codes[node.symbol] = new_val

        return codes



# if __name__ == '__main__':
#     res = ShannonFano('word')
#     print(res)
