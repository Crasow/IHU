
def float2bin(x, eps=1e-9):
    res = ''
    while x > eps:
        x *= 2
        res += str(int(x))
        x -= int(x)

    return res


def bin2float(x):
    return sum(2 ** (-i - 1) for i, digit in enumerate(x) if digit == '1')


def find_code(a, b):
    i = 0
    a += '0' * (len(b) - len(a))
    while a[i] == b[i]:
        i += 1
    res = a[:i] + '0'
    cnt = 0
    while a[i] == 1:
        i += 1
        cnt += 1
    res += '1' * (cnt + 1)
    return res


def coding(word, alphabet, prob):
    left, right = 0, 1

    for letter in word:
        letter_indx = alphabet.index(letter)
        left, right = (left + (right - left) * sum(prob[:letter_indx]),
                       left + (right - left) * sum(prob[: letter_indx + 1]))

    a,b = map(float2bin, (left, right))
    # res = find_code(res)
    return find_code(a,b)
    # return left, right


alphabet = 'abc'
prob = (4 / 7, 2 / 7, 1 / 7)
word = 'abacaba'
code = coding(word, alphabet, prob)
print(code)
