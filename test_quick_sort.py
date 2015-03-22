# -*- coding: utf-8 -*-
from quick_sort import quick_sort


def test_sorted():
    my_list = list(range(100))
    quick_sort(my_list)
    assert my_list == list(range(100))


def test_reverse():
    my_list = list(range(100))[::-1]
    quick_sort(my_list)
    assert my_list == list(range(100))


def test_empty():
    my_list = []
    quick_sort(my_list)
    assert my_list == []


def test_abc():
    my_list = ['a', 'b', 'c', 'd', 'e']
    quick_sort(my_list)
    assert my_list == ['a', 'b', 'c', 'd', 'e']
    my_list = ['e', 'd', 'c', 'b', 'a']
    quick_sort(my_list)
    assert my_list == ['a', 'b', 'c', 'd', 'e']


def test_unicode():
    my_list = ['π']
    quick_sort(my_list)
    assert my_list == ['\xcf\x80']


def test_duplicate():
    my_list = [1, 2, 2, 5, 3]
    quick_sort(my_list)
    assert my_list == [1, 2, 2, 3, 5]


def test_combo():
    my_list = [42, 1, 'a', 500]
    quick_sort(my_list)
    assert my_list == [1, 42, 500, 'a']
    my_list = [42, '1', 'a', '500']
    quick_sort(my_list)
    assert my_list == [42, '1', '500', 'a']


def test_function():
    my_list = []
    new_list = [quick_sort(my_list)]
    assert new_list == [None]
