def quick_sort(lst):
    _quick_sort(lst, 0, len(lst) - 1)


def _quick_sort(lst, left, right):
    if left < right:
        pivot = _partition(lst, left, right)
        _quick_sort(lst, left, pivot - 1)
        _quick_sort(lst, pivot + 1, right)


def _partition(lst, left, right):
    if right == -1:
        right = len(lst) - 1
    pivot = _pivot_picker(lst, left, right)
    lst[pivot], lst[right] = lst[right], lst[pivot]
    boundary = left
    for i in range(left, right):
        if lst[i] < lst[right]:
            lst[i], lst[boundary] = lst[boundary], lst[i]
            boundary += 1
    lst[right], lst[boundary] = lst[boundary], lst[right]
    return boundary


def _pivot_picker(lst, left, right):
    if right == -1:
        right = len(lst) - 1
    mid = len(lst) // 2
    if lst[left] <= lst[mid] <= lst[right] or lst[left] >= lst[mid] >= lst[right]:
        return mid
    elif lst[mid] <= lst[left] <= lst[right] or lst[mid] >= lst[left] >= lst[right]:
        return left
    else:
        return right

if __name__ == '__main__':
    ml = [1, 10, 4, 14, 12, 7, 4, 6]
    quick_sort(ml)
    print ml
