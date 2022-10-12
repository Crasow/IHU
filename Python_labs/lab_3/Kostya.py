import math as m

"""
First task
"""
x = -3
x_max = 3
step = 0.2
a = 0.5
for el in range(4):
    while True:
        try:
            y = a * x / a + m.pow(1 + m.pow(x, 2), 1 / 3)
        except ZeroDivisionError:
            print('Can`t divide by zero')
            x = x + step
            continue
        print(y, end=' ')
        x = x + step
        if x > x_max:
            break
    a += 0.25
    x = 0
    print()
    print()

"""
Second task
"""

x = 2
factor_cnt = 1
pow = 2
row_sum = 0
n = 2

while True:
    factor = 1
    for el in range(1, n + 1):
        factor *= el

    cycle_part = m.pow(2, pow) * m.pow(x, pow) / factor
    if abs(cycle_part) < m.pow(10, -6):
        break

    row_sum += cycle_part
    pow += 2
    n += 2

row_sum = 1 - row_sum
print(row_sum)
