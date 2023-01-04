def dict_parsing(res_dict):
    key = ''
    user_answer = input('1 - step by step, 2 - if you have ready dictionary: ')
    if user_answer == '1':
        print('Write !- to stop')
        while True:
            key = input('Write symbol: ')
            if key == '!-':
                break
            value = input('Write it`s code: ')
            res_dict[key] = value
    if user_answer == '2':
        user_answer = input('Enter you dict\n')
        var = user_answer.replace('{', '')
        var = var.replace('}', '')
        var = var.replace("'", '')
        var = var.replace(" ", '')
        var = var.replace(",", ':')
        var = var.split(':')
        for el in range(0, len(var) - 1, 2):
            res_dict[var[el]] = var[el + 1]

    return res_dict


def main():
    code = input('Write code: ')
    code_dict = {}
    code_dict = dict_parsing(code_dict)

    res = ''
    var = ''
    cnt = 0

    for el in range(cnt, len(code)):
        var += code[el]
        for k, v in code_dict.items():
            if var == v:
                res += k
                var = ''
                break

    print('-' * 50)
    print(f'Your word is {res}')
    input('')


if __name__ == '__main__':
    main()
