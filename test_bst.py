from bst import BinarySearchTree


nodes = [5, 4, 8, 3, 43, 22, 7, 74, 2]


def test_insert_nodes():
    """size of tree equal to number of values inserted"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
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


def test_balance():
    """balance updated when node added"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    assert b.balance() == 0
    b.insert(90)
    assert b.balance() == 1


def test_depth():
    """depth updated as nodes added"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    assert b.depth() == 4
    b.insert(90)
    assert b.depth() == 5


def test_size():
    """size on empty and when populated"""
    b = BinarySearchTree()
    assert b.size() == 0
    for n in nodes:
        b.insert(n)
    assert b.size() == 9


def test_root():
    """check tree's root and child nodes"""
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    assert b.root.val == 5
    assert b.root.left.val == 4
    assert b.root.right.val == 8
