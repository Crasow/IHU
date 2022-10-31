from collections import Counter
import operator


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
        self.calculate_probability()
        self.tree_create()
        self.encode_symbols(self.end_node)
        encoded_data = ''
        for el in self.user_data:
            for key in self.symbol_codes_dict.keys():
                if el == key:
                    encoded_data += self.symbol_codes_dict[key]
                    encoded_data += ' '
        sorted_codes_dict = sorted(self.symbol_codes_dict.items(), key=lambda item: len(item[1]))

        return encoded_data, sorted_codes_dict


if __name__ == "__main__":
    # a = Huffman('телефонеон')
    print(Huffman('телефонеон').code_output())

    # print(huff_obj.symbol_codes_dict)
