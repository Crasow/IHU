from random import randint


def create_arr(arr_length, from_, to_):
    arr = [randint(from_, to_) for el in range(arr_length)]
    return arr


def add_ones(array, from_):
    for el in range(from_, len(array)):
        array[el] = 1
    return array


def arr_min(arr):
    minimal_el = arr[0]
    for el in arr:
        if minimal_el > el:
            minimal_el = el
    return minimal_el


def main():
    array = create_arr(10, 0, 40)
    changed_array = add_ones(array, 4)
    minimal_element = arr_min(changed_array)
    print(array)
    print(changed_array)
    print(minimal_element)


if __name__ == '__main__':
    main()
