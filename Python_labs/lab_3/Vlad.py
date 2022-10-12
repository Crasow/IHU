import math as m

"""
First task
"""
x_max = 3
x = 0
step = 0.1
a = 0.5
for el in range(4):
    while True:
        try:
            y = m.atan(x / 2 * a) / pow(x, 2) + 2 * a
        except ZeroDivisionError:
            print('Can`t divide by zero', end=' ')
            x = x + step
            continue
        print(y, end=' ')
        x = x + step
        if x > x_max:
            break
    a += 0.25
    x = 0
    print()

"""
Second task
"""

x = 2
factor = 1
factor_cnt = 1
power = 1
in_log = 1
row_sum = 1 + x * m.log(2) / 1

while True:
    factor_cnt += 1
    factor *= factor_cnt
    in_log += 1
    power += 1
    cycle_part = m.pow(x, power) * m.pow(m.log(in_log), power) / float(factor)
    if abs(cycle_part) < m.pow(10, -6):
        break
    row_sum += cycle_part

print(f'{row_sum}')
