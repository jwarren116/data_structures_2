def quick_sort(my_list):
    _quick_sort(my_list, 0, len(my_list) - 1)


def _quick_sort(my_list, left, right):
    if len(my_list) <= 1:
        pivot = _pivot_picker(my_list, left, right)
        _quick_sort(my_list, pivot + 1, right)
        _quick_sort(my_list, left, pivot - 1)


def _pivot_picker(lst, left, right):
    mid = len(lst) // 2

    if lst[left] <= lst[mid] <= lst[right] or lst[left] >= lst[mid] >= lst[right]:
        return mid
    elif lst[mid] <= lst[left] <= lst[right] or lst[mid] >= lst[left] >= lst[right]:
        return left
    else:
        return right

if __name__ == '__main__':
    ml = [10, 2, 1, 4]
    ml2 = [2, 1, 3]
    ml3 = [3, 1, 2]
    ml4 = [3, 2, 1]
    ml5 = [1, 3, 2]
    ml6 = [2, 3, 1]

    print _pivot_picker(ml)
    print _pivot_picker(ml2)
    print _pivot_picker(ml3)
    print _pivot_picker(ml4)
    print _pivot_picker(ml5)
    print _pivot_picker(ml6)
