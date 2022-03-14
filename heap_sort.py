import math
import sys


def heap_sort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, -1, -1):
        swap(array, 0, i)
        heapify(array, 0, right_bound_index=(i - 1))


def build_max_heap(array):
    middle_pos = math.floor(len(array) / 2)
    middle_index = middle_pos - 1

    # Every number to the right of `middle_index` is the bottom leaf nodes,
    # so we iterate from `middle_index` to 0 and `heapify` each node, from the bottom up.
    for i in range(middle_index, -1, -1):
        heapify(array, i)


def heapify(array, parent_node_index, right_bound_index=None):
    """
    Given an array and an index of the parent node, create a max heap where
    from that parent node down to all of its child nodes, every parent node is greater than its 2 child nodes
    """
    if right_bound_index is None:
        right_bound_index = len(array) - 1

    left_child_index = parent_node_index * 2
    right_child_index = left_child_index + 1

    parent_value = array[parent_node_index]
    max_value = parent_value
    max_value_index = parent_node_index

    if left_child_index < len(array[:right_bound_index + 1]):
        left_value = array[left_child_index]
        if left_value > max_value:
            max_value = left_value
            max_value_index = left_child_index

    if right_child_index < len(array[:right_bound_index + 1]):
        right_value = array[right_child_index]
        if right_value > max_value:
            max_value = right_value
            max_value_index = right_child_index

    if max_value_index != parent_node_index:
        swap(array, max_value_index, parent_node_index)
        heapify(array, max_value_index, right_bound_index=right_bound_index)


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
        arg = '285391'
    array = list(map(int, arg))
    heap_sort(array)
    print(*array, sep='')
