from random import randint


def create_arr(arr_length, from_int, to_int):
    arr = [randint(from_int, to_int) for el in range(arr_length)]
    return arr


def create_new_arr(arr_donor, from_int, to_int):

    new_arr = [arr_donor[el] for el in range(from_int, to_int)]
    return new_arr


def arr_sum(arr):
    res = 0
    for el in arr:
        res += el
    return res


def main():
    base_arr = create_arr(10, 4, 46)
    new_arr = create_new_arr(base_arr, 3, 9)
    new_arr_sum = arr_sum(new_arr)
    print(base_arr)
    print(new_arr)
    print(new_arr_sum)


if __name__ == '__main__':
    main()
