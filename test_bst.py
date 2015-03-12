from bst import BinarySearchTree
import pytest


nodes = [5, 4, 8, 3, 43, 22, 7, 74, 2]


def test_insert_nodes():
    """size of tree equal to number of values inserted"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    assert b.contains(5)
    assert b.contains(43)
    assert b.contains(2)
    assert b.size() == 9


def test_contains_node():
    """expected nodes in tree"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    assert b.contains(74)
    assert b.contains(2)
    assert b.contains(5)
    assert b.contains(43)
    assert not b.contains(103)


# def test_balance():
#     """balance updated when node added"""
#     b = BinarySearchTree()
#     for n in nodes:
#         b.insert(n)
#     assert b.balance() == 0
#     b.insert(90)
#     assert b.balance() == 0


def test_depth():
    """depth updated as nodes added"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    assert b.depth() == 4
    b.insert(90)
    assert b.depth() == 4


def test_size():
    """size on empty and when populated"""
    b = BinarySearchTree()
    assert b.size() == 0
    for n in nodes:
        b.insert(n)
    assert b.size() == 9


# def test_root():
#     """check tree's root and child nodes"""
#     b = BinarySearchTree()
#     for n in nodes:
#         b.insert(n)
#     assert b.root.val == 7
#     assert b.root.left.val == 3
#     assert b.root.right.val == 74


def test_in_order():
    """Test the in order traversal method of a BST"""
    assertions = [2, 3, 4, 5, 7, 8, 22, 43, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()


# def test_pre_order():
#     """Test the pre order traversal method of a BST"""
#     assertions = [7, 3, 2, 4, 5, 74, 8, 43, 22]
#     b = BinarySearchTree()
#     for n in nodes:
#         b.insert(n)
#     actual = b.pre_order()
#     for val in assertions:
#         assert actual.next() == val
#     with pytest.raises(StopIteration):
#         actual.next()


# def test_post_order():
#     """Test the post order traversal method of a BST"""
#     assertions = [2, 5, 4, 3, 8, 22, 43, 74, 7]
#     b = BinarySearchTree()
#     for n in nodes:
#         b.insert(n)
#     actual = b.post_order()
#     for val in assertions:
#         assert actual.next() == val
#     with pytest.raises(StopIteration):
#         actual.next()


# def test_breadth_first():
#     """Test the breadth first traversal method of a BST"""
#     assertions = [7, 3, 74, 2, 4, 8, 43, 5, 22]
#     b = BinarySearchTree()
#     for n in nodes:
#         b.insert(n)
#     actual = b.breadth_first()
#     for val in assertions:
#         assert actual.next() == val
#     with pytest.raises(StopIteration):
#         actual.next()


def test_delete_root():
    """Test the in order traversal method of a BST"""
    assertions = [2, 3, 4, 7, 8, 22, 43, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    b.delete(5)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()


def test_delete_with_no_children():
    """Test the in order traversal method of a BST"""
    assertions = [2, 3, 4, 5, 7, 8, 43, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    b.delete(22)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()


def test_delete_with_left_child():
    """Test the in order traversal method of a BST"""
    assertions = [2, 4, 5, 7, 8, 22, 43, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    b.delete(3)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()


def test_delete_with_two_children():
    """Test the in order traversal method of a BST"""
    assertions = [2, 3, 4, 5, 7, 8, 22, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    b.delete(43)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()


def test_multiple_delete():
    """Test the in order traversal method of a BST"""
    assertions = [2, 3, 4, 5, 7, 22, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    b.delete(43)
    b.delete(8)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()


def test_self_balance_one_leg():
    """test rebalancing when nodes inserted in ascending order"""
    b = BinarySearchTree()
    for n in range(15):
        b.insert(n)
    assert b.balance() == 0


def test_self_balance_with_delete():
    """test rebalancing after deleting nodes"""
    b = BinarySearchTree()
    for n in range(15):
        b.insert(n)
    b.delete(7)
    b.delete(1)
    assert b.balance() == 0


def test_self_balance_with_insert():
    """test rebalancing after inserting higher nodes"""
    assertions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22, 23, 24]
    b = BinarySearchTree()
    for n in range(15):
        b.insert(n)
    b.insert(22)
    b.insert(23)
    b.insert(24)
    assert b.balance() == 0
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val
    with pytest.raises(StopIteration):
        actual.next()
