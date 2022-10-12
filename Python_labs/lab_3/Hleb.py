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
    print('-' * 50)

"""
Second task
"""
up_num = 1
x = 0.5
up = 1 * m.pow(x, 3)

bot_nums = [2, 3]

row_sum = 0

while True:
    bot = 1

    for el in bot_nums:
        bot *= el

    try:
        cycle_part = up / bot
    except ZeroDivisionError:
        print('Can`t divide by zero')
        continue

    if abs(cycle_part) < m.pow(10, -6):
        break

    up_num += 2
    up *= up_num * 4

    bot_nums[-1] += 1
    bot_nums.append(bot_nums[-1] + 1)

    if len(bot_nums) % 2 == 0:
        row_sum += cycle_part
    else:
        row_sum -= cycle_part

row_sum = x / 1 + row_sum
print(row_sum)
