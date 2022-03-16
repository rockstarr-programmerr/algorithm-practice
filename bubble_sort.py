import sys


def bubble_sort(array):
    for i in range(len(array) - 1):
        # After each iteration, one more number is "bubbled" to the sorted partition at the end of the array.
        # So the `right_bound_index` is subtracted by `i`.
        # But then we only need to iterate to the second-to-last element of the unsorted partition,
        # so subtract `right_bound_index` further by 2.
        right_bound_index = len(array) - i - 2

        for left_index in range(len(array[:right_bound_index + 1])):
            right_index = left_index + 1

            left_number = array[left_index]
            right_number = array[right_index]

            if left_number > right_number:
                swap(array, left_index, right_index)


def swap(array, index1, index2):
    if index1 == index2:
        return

    left_index = min(index1, index2)
    right_index = max(index1, index2)

    # NOTE: The left-right or right-left order of execution below is significant,
    # because it ensure the correct value is inserted to the correct index.
    right_value = array.pop(right_index)
    left_value = array.pop(left_index)
    array.insert(left_index, right_value)
    array.insert(right_index, left_value)


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = '285553941'
    array = list(map(int, arg))
    bubble_sort(array)
    print(*array, sep='')
