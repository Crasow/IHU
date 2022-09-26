from collections import Counter


def main():
    # Ask user a word
    user_word = input('Enter you word: ')
    if not user_word:
        user_word = 'телефон'

    # Creating list of tuples with pairs (symbol, qty in word)
    word_counter = sorted(Counter(user_word).items())

    # Creating list with lists [symbol, qty in word, space for code]
    for indx, el in enumerate(word_counter):
        word_counter[indx] = list(el) + ['']

    code = []  # result [symbol, qty in word, code]

    code_dict = {}  # comfortable dict {symbol:code}
    encoded_word = ''  # readable code

    def encoding(arr):
        left, right = [], []

        # Sum of symbol frequencies in a word
        freq_sum = 0
        for i, el in enumerate(arr):
            freq_sum += el[1]

        # check for only 1 incoming value
        if len(arr) == 1:
            arr[0][2] += '0'
            code.append(arr)
            return

        # Find index of middle symbol by frequnce
        sum = 0
        for el in range(len(arr)):
            sum += arr[el][1]
            if sum * 2 >= freq_sum:
                half_indx = el + (abs(2 * sum - freq_sum) < abs(2 * (sum - arr[el][1]) - freq_sum))
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
            code.append(left)
        else:
            encoding(left)  # recursion for left part until there will be only 1 el
        if len(right) == 1:  # second exit condititon
            code.append(right)
        else:
            encoding(right)

    encoding(word_counter)
    for el in range(len(user_word)):
        for c_el in range(len(code)):
            if user_word[el] == code[c_el][0][0]:
                encoded_word += code[c_el][0][2] + ' '

    for el in range(len(code)):
        code_dict[code[el][0][0]] = code[el][0][2]

    encoding(word_counter)
    print(encoded_word)
    print(code_dict)
    input('')


if __name__ == '__main__':
    main()
