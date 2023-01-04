from collections import Counter


class Huffman:
    def __init__(self, user_data):
        self.user_data = user_data
        self.sym_prob = {}
        self.nodes = []

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

        for k in sym_freq.keys():
            self.sym_prob[k] = (sym_freq[k] / len(self.user_data))
        print(sym_freq)
        print(self.sym_prob)
        return self.sym_prob

    def create_node_list(self):
        for k, v in self.sym_prob.items():
            self.nodes.append(self.Node(symbol=k, prob=v))
        return self.nodes
        # for el in range(len(self.self.nodes)):
        # print(self.self.nodes[el].symbol, end=' ')
        # print(self.self.nodes[el].freq)

    def tree_create(self, nodes):
        nodes = sorted(nodes, key=lambda x: x.prob)
        left = nodes.pop(0)
        right = nodes.pop(0)

        left.code = '0'
        right.code = '1'

        nodes.append(self.Node(symbol=left.symbol + right.symbol,
                               prob=left.prob + right.prob,
                               left=left, right=right))

        if len(nodes) == 1:
            return nodes[0]
        """
        WHY THIS PART IS WORKING
        """
        self.tree_create(nodes)


    def encode_symbols(self, node, code=''):
        symbol_codes_dict = {}
        symbol_code = code + node.code

        if node.left:
            self.encode_symbols(nodes.left, symbol_code)
        if node.right:
            self.encode_symbols(nodes.right, symbol_code)

        if not node.left and not node.right:
            symbol_codes_dict[node.symbol] = symbol_code
        print(symbol_codes_dict)
        return symbol_codes_dict

if __name__ == "__main__":
    huff_obj = Huffman('телефонеон')
    huff_obj.calculate_probability()
    nodes_list = huff_obj.create_node_list()
    final_node = huff_obj.tree_create(nodes_list)
    huff_obj.encode_symbols(final_node)
