from encoder import Huffman

huff_obj = Huffman('arararrar')
var = huff_obj.calculate_probability()
print(var)
arr = []
my_str = ''
for k in var.keys():
    my_str += k

print(my_str)
for el in my_str:
    for ell in my_str:
        arr.append([el, ell])

range_var = 2
cnt = 0
cons_arr = []
while cnt < pow(len(my_str),range_var):
    cons_arr.append([])
    cnt += 1

recur_cnt = 0
cnt = 0
# while cnt <=len(my_str):
# def recurs(arr, cnt):
#     if recur_cnt >= pow(len(my_str),range_var):
#         return
#     else:
#         for el in arr:
#             cons_arr[cnt].append()
#


print(cons_arr)
print(len(cons_arr))
print(arr)
print(len(arr))

