import math

n = 1
x = math.pi * 4
cycle_part_sum = 0

while True:

    factor = 1
    for el in range(1, 2 * n + 1):
        factor *= el

    cycle_part = pow(-1, n) * (pow(2, 2 * n) * pow(x, 2 * n + 1) / factor)

    if abs(cycle_part) < pow(10, -6):
        break

    cycle_part_sum += cycle_part
    n += 1


res = x + cycle_part
print(res)

y = x * math.cos(2 * x)
print(y)
