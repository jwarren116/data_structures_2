# -*- coding: utf-8 -*-
from radix_sort import int_radix, str_radix


def test_sorted():
    my_list = list(range(100))
    new_list = int_radix(my_list)
    assert new_list == list(range(100))


def test_reverse():
    my_list = list(range(100))[::-1]
    new_list = int_radix(my_list)
    assert new_list == list(range(100))


def test_empty():
    my_list = []
    new_list = str_radix(my_list)
    assert new_list == []


def test_abc():
    my_list = ['a', 'b', 'c', 'd', 'e']
    new_list = str_radix(my_list)
    assert new_list == ['a', 'b', 'c', 'd', 'e']
    my_list = ['e', 'd', 'c', 'b', 'a']
    new_list = str_radix(my_list)
    assert new_list == ['a', 'b', 'c', 'd', 'e']


def test_words():
    my_list = ['apple', 'berry', 'candle', 'deck', 'equal']
    new_list = str_radix(my_list)
    assert new_list == ['apple', 'berry', 'candle', 'deck', 'equal']
    my_list = ['equal', 'deck', 'candle', 'berry', 'apple']
    new_list = str_radix(my_list)
    assert new_list == ['apple', 'berry', 'candle', 'deck', 'equal']


def test_mixed_case():
    my_list = ['doG', 'Apple', 'aPPle', 'DOG', 'anVIL', 'applE']
    new_list = str_radix(my_list)
    assert new_list == ['anVIL', 'Apple', 'aPPle', 'applE', 'doG', 'DOG']


def test_duplicate():
    my_list = [1, 2, 2, 5, 3]
    new_list = int_radix(my_list)
    assert new_list == [1, 2, 2, 3, 5]
