string = 'Some, int-er. ge-r? Word getaout'

list_string = string.split()

new_str = ''
for el in list_string:
    new_str += el[0]

print(new_str)

for el in list_string:
    print(f'{el} - {len(el)}', end='')
print()

sorted_lst_string = list_string.copy()
sorted_lst_string.sort()
# sorted_lst_string.reverse()
for el in sorted_lst_string:
    print(el, end=' ')
print()

new_str = string
signs = '!()-[]{};?@#$%:\'\"\,./^;*_'
for el in signs:
    new_str = new_str.replace(el, '')
print(new_str)

signs_dict = {'.': 'крапка', ',': 'кома', '?': 'знак питання', '-': 'тире'}
new_str = string
for key in signs_dict.keys():
    new_str = new_str.replace(key, signs_dict[key])
print(new_str)

temp = list_string.pop()
list_string.insert(1, temp)
temp = list_string.pop(2)
list_string.append(temp)

for el in list_string:
    print(el, end=' ')
