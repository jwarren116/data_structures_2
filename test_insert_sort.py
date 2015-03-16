# -*- coding: utf-8 -*-
import pytest
from insert_sort import insert_sort


def test_sorted():
    my_list = list(range(100))
    insert_sort(my_list)
    assert my_list == list(range(100))


def test_reverse():
    my_list = list(range(100))[::-1]
    insert_sort(my_list)
    assert my_list == list(range(100))


def test_empty():
    my_list = []
    insert_sort(my_list)
    assert my_list == []


def test_abc():
    my_list = ['a', 'b', 'c', 'd', 'e']
    insert_sort(my_list)
    assert my_list == ['a', 'b', 'c', 'd', 'e']
    my_list = ['e', 'd', 'c', 'b', 'a']
    insert_sort(my_list)
    assert my_list == ['a', 'b', 'c', 'd', 'e']


def test_unicode():
    my_list = ['π']
    insert_sort(my_list)
    assert my_list == ['\xcf\x80']


def test_duplicate():
    my_list = [1, 2, 2, 5, 3]
    insert_sort(my_list)
    assert my_list == [1, 2, 2, 3, 5]


def test_combo():
    my_list = [42, 1, 'a', 500]
    insert_sort(my_list)
    assert my_list == [1, 42, 500, 'a']
    my_list = [42, '1', 'a', '500']
    insert_sort(my_list)
    assert my_list == [42, '1', '500', 'a']


def test_function():
    my_list = []
    new_list = [insert_sort(my_list)]
    assert new_list == [None]


def test_non_iterable():
    with pytest.raises(TypeError):
        insert_sort(42)
