#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def merge_sort(lyst):
    buf = [None for x in range(len(lyst))]
    _merge_sort(lyst, buf, 0, len(lyst)-1)


def _merge_sort(lyst, buf, low, high):
    if low < high:
        middle = (low + high) // 2
        _merge_sort(lyst, buf, low, middle)
        _merge_sort(lyst, buf, middle+1, high)
        merge(lyst, buf, low, middle, high)


def merge(lyst, buf, low, middle, high):
    i1 = low
    i2 = middle + 1

    for i in range(low, high+1):
        if i1 > middle:
            buf[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            buf[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            buf[i] = lyst[i]
            i1 += 1
        else:
            buf[i] = lyst[i2]
            i2 += 1
    for i in range(low, high+1):
        lyst[i] = buf[i]


if __name__ == '__main__':
    import timeit
    import random

    best_list = [i for i in range(1000)]
    worst_list = [i for i in range(1000)]
    random.shuffle(worst_list)
    tim_list = [i for i in range(1000)]
    random.shuffle(tim_list)

    def best_case():
        return merge_sort(best_list)

    def worst_case():
        return merge_sort(worst_list)

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
    print tim_list
    print "Timsort! {}: {}\nWhoa...".format(len(tim_list),
                                            timeit.timeit('tim_list.sort()',
                                            setup='from __main__ import tim_list',
                                            number=100)
                                            )