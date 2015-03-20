# -*- coding: utf-8 -*-
from merge_sort import merge_sort


def test_sorted():
    my_list = list(range(100))
    merge_sort(my_list)
    assert my_list == list(range(100))


def test_reverse():
    my_list = list(range(100))[::-1]
    merge_sort(my_list)
    assert my_list == list(range(100))


def test_empty():
    my_list = []
    merge_sort(my_list)
    assert my_list == []


def test_abc():
    my_list = ['a', 'b', 'c', 'd', 'e']
    merge_sort(my_list)
    assert my_list == ['a', 'b', 'c', 'd', 'e']
    my_list = ['e', 'd', 'c', 'b', 'a']
    merge_sort(my_list)
    assert my_list == ['a', 'b', 'c', 'd', 'e']


def test_unicode():
    my_list = ['π']
    merge_sort(my_list)
    assert my_list == ['\xcf\x80']


def test_duplicate():
    my_list = [1, 2, 2, 5, 3]
    merge_sort(my_list)
    assert my_list == [1, 2, 2, 3, 5]
