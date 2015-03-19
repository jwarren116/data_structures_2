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
