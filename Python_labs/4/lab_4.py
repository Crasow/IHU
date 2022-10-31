import random

mtrx = [random.randint(4, 20) for el in range(10)]
print(mtrx)

new_arr = [el for el in mtrx if el > 4 and el <= 9]
print(new_arr)

new_arr_sum = 0
for el in new_arr:
    new_arr_sum+= el
print(new_arr_sum)

print('\n')

mtrx = []
for el in range (10):
    row = []
    for j in range(8):
        row.append(0+random.randint(-16,43))
    mtrx.append(row)

print('Matrix looks like:')

for row in mtrx:
    for el in row:
        print('%.f' % el, end='\t\t')
    print()

print('Technical look of matrix:')
print(mtrx)

new_mtrx = []

temp =0
for el in mtrx[1]:
    temp += el
new_mtrx.append(temp)

temp= 0
for el in mtrx[3]:
    temp -= el
new_mtrx.append(temp)

temp = 1
for el in mtrx:
    temp *= el[4]
new_mtrx.append(temp)

temp = 1
for el in mtrx:
    temp /= el[6]
new_mtrx.append(temp)

print(new_mtrx)