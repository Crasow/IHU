# -*- coding: utf-8 -*-
"""lab_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Og_Xbui9Nmu8mQkVxolwYqEkFge-rzJ3
"""

import math

"""1"""

x = -1
y = -2
if 1 <= x <= 2 and 1 <= y <= 2 or \
        -2 <= x < -1 and 1 <= y <= 2 or \
        1 <= x <= 2 and -2 <= y <= -1 or \
        -2 <= x <= -1 and -2 <= y <= -1:
    print('good')
else:
    print('wtf')

"""2"""

num = 909
all_are_even = [0, 0, 0]
summ = 0
for el in range(len(str(num))):
    summ += int(str(num)[el])
    var = int(num) % 2
    if var == 0:
        all_are_even[el] = 1

if '2' in str(num):
    print('2 is present')

if 0 in all_are_even:
    pass
else:
    print('all nums are even')

if summ == 18:
    print('sum of numbers = 18')

"""3"""

x = 10

if x <= 0:
    x = 0
elif 0 < x <= 1:
    x = x * x
elif x > 1:
    x = x * x * x * x

"""4"""

x = 10
y = 10
if x == 0 and y == 0:
    print('Noone')
elif x > 0 and y > 0:
    print(1)
elif x < 0 < y:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y > 0:
    print(4)

"""5"""

x = 2
y = 3

if abs(x) <= y and y > 0:
    print('Da')

if -1 <= x <= 1 and -1 <= y <= 1:
    print('Da')

if 0 <= x <= 2 and 0 <= y <= 1:
    print('Da')

if abs(x) < 2 * math.pi * 2 and x < 0 and -2 <= y <= 2 \
        or abs(y) >= x > 0 and -2 <= y <= 2:
    print('Da')

"""6"""

month = 9

even_odd = month % 2

if month == 2:
    print(28)
elif month < 8:
    if even_odd == 0:
        print(30)
    else:
        print(31)
elif month >= 8:
    if even_odd == 0:
        print(31)
    else:
        print(30)

"""7"""

k = 9
print(f'We found {k} mushrooms in the forest')

"""8"""

n = 0

if x < 0 < y:
    n = 3
elif y < 0 < x:
    n = 4
elif x > 0 and y > 0:
    if y >= x * x * x:
        n = 1
    else:
        n = 4
elif x < 0 and y < 0:
    if y <= x * x * x:
        n = 2
    else:
        n = 3

print(f"Your dot is in {n} part")