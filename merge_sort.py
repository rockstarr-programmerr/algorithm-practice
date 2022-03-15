import math
import sys


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle_pos = math.floor(len(array) / 2)
    array1 = array[:middle_pos]
    array2 = array[middle_pos:]

    sorted_array1 = merge_sort(array1)
    sorted_array2 = merge_sort(array2)

    sorted_array = merge(sorted_array1, sorted_array2)
    return sorted_array


def merge(array1, array2):
    """
    Merge 2 orderred arrays into 1 orderred array.
    """
    merged_array = []

    while len(array1) and len(array2):
        if array1[0] < array2[0]:
            merged_array.append(array1.pop(0))
        else:
            merged_array.append(array2.pop(0))

    # At this point, one of `array1` or `array2` is empty.
    # Since `array1` and `array2` are assumed to be orderred,
    # we can just extend `merged_array` with the rest of them.
    merged_array.extend(array1)
    merged_array.extend(array2)

    return merged_array


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = '28539417'
    array = list(map(int, arg))
    sorted_array = merge_sort(array)
    print(*sorted_array, sep='')
