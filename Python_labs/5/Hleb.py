string = 'Some int-er ge-r Word getaout'

str_list = string.split()

big_let_words = []
for el in str_list:
    if ord(el[0]) in range(ord('A'), ord('Z') + 1):
        big_let_words.append(el)
print(big_let_words)

a_word_cnt = 0
for el in str_list:
    if 'a' in el:
        a_word_cnt += 1
print(a_word_cnt)

same_letter_start_end_word_cnt = 0
for el in str_list:
    if el[0] == el[-1]:
        same_letter_start_end_word_cnt += 1
print(same_letter_start_end_word_cnt)

words_len_more_five = []
for el in str_list:
    if len(el) > 5:
        words_len_more_five.append(el)
print(words_len_more_five)

new_str = ''
for el in str_list:
    new_str += f'{el[::-1]} '
print(new_str)

new_str = ''
for el in str_list:
    if '-' in el:
        new_str += f'{el} '
print(new_str)