import time

x = [1, 2, 3, 4, 5]
y = [3, 1, 5, 4, 2]
number = 554

print('')


def first(arr_x, arr_y):
    print('x', end=' | ')
    for el in range(len(arr_x) - 1):
        print(arr_x[el], end=' | ')
    print(arr_x[-1])

    print('---+' * 5)

    print('y', end=' | ')
    for el in range(len(arr_y) - 1):
        print(arr_y[el], end=' | ')
    print(arr_y[-1])


def second(num):
    num = str(num)
    res = 0
    for el in num:
        res += int(el)
    return res


def third():
    print('a)')
    print('a)\n    *\n  * * *\n* * * * *\n  * * *\n    *')
    print('b)\n* * * * *\n* *   * *\n*   *   *\n* *   * *\n* * * * *')
    print('c)\n    *******\n  *         *\n*    Hello    *\n  *         *\n    *******')


def fourth():
    print('a)\na   a   a\n  a   a\na   a   a')
    print('b)\na-------a\n|   a   |\na-------a')


def five():
    a = 10
    b = 5
    c = 7
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(int(s))


def six():
    a = 20
    b = 20
    c = 100
    y = (c + (a / (a ** 2 + b ** 2))) / (a + (b / (b ** 2 + c ** 2)))
    print(int(y))


def seven():
    a = 10
    b = 15
    c = 5
    d = (b ** 2 - 4 * a * c) ** 0.5
    x1 = (-b + d) / 2 * a
    x2 = (-b - d) / 2 * a
    print(int(x1), int(x2))


def eight():
    n = input('Введите вариант примера: ')
    if n == 'a' or n == 'b' or n == 'c':
        x = int(input('Введите число x: '))
        y = int(input('Введите число y: '))

        if n == 'a':
            f = x ** 3 + 3 * x ** 2 * y + 3 * x * y ** 2 + y ** 3
        elif n == 'b':
            f = x ** 2 * y ** 2 + x ** 3 * y ** 3 + x ** 4 * y ** 4
        elif n == 'c':
            f = x + y + x ** 2 + y ** 2 + x ** 3 + y ** 3 + x ** 4 + y ** 4
        print(f)
    else:
        a = 1000
        while True:
            print(f'Ты не прав')
            b = a - 7
            print(f'{a}-7={b}')
            a = b
            time.sleep(0.1)

first(x, y)
print('\r', second(number), sep='')
third()
fourth()
five()
six()
seven()
eight()