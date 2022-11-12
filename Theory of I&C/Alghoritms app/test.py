import argparse
from struct import *

mode = ''
file_paths = []
arch_path = ''


class Compressor:
    def __init__(self, file_paths, arch_path):
        self.file_paths = file_paths
        self.arch_path = arch_path

    def readFile(self, path):
        input_file = open(path, 'rt')
        data = input_file.read()
        input_file.close()
        return data

    def compressData(self, data, dictionary, dict_size):
        compessed_data = []
        string = ''
        for symbol in data:
            new_string = string + symbol
            if new_string in dictionary:
                string = new_string
            else:
                compessed_data.append(dictionary[string])
                dictionary[new_string] = dict_size
                dict_size += 1
                string = symbol

        if string in dictionary:
            compessed_data.append(dictionary[string])
        return compessed_data

    def writeFile(self, compressed_data):
        output_file = open(self.arch_path, 'wb')
        for data in compressed_data:
            output_file.write(pack('>H', int(data)))
        output_file.close()

    def compress(self):
        for path in self.file_paths:
            dict_size = 256
            dictionary = {chr(i): i for i in range(dict_size)}
            data = self.readFile(path)
            compressed_data = self.compressData(data, dictionary, dict_size)
            self.writeFile(compressed_data)


if __name__ == '__main__':
    args = parseCmdArgs(sys.argv)
    if args.mode == 'pack':
        pass
        # Compressor( < путь к файлу >, < путь к архиву >).compress()