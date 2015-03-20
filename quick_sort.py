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
    import timeit

    best_list = [i for i in range(1000)]
    worst_list = [i for i in range(999)]
    worst_list.insert(0, 1000)

    def best_case():
        return quick_sort(best_list)

    def worst_case():
        return quick_sort(worst_list)

    print "Best case of {}: {}".format(len(best_list),
                                       timeit.timeit('best_case()',
                                       setup='from __main__ import best_case',
                                       number=100)
                                       )
    print "Worst case of {}: {}".format(len(worst_list),
                                        timeit.timeit('worst_case()',
                                        setup='from __main__ import worst_case',
                                        number=100)
                                        )

    print "Timsort! {}: {}\nWhoa...".format(len(worst_list),
                                        timeit.timeit('worst_list.sort()',
                                        setup='from __main__ import worst_list',
                                        number=100)
                                        )
