from bst import BinarySearchTree


nodes = [5, 4, 8, 3, 43, 22, 7, 74, 2]


def test_in_order():
    """"""
    assertions = [2, 3, 4, 5, 7, 8, 22, 43, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    actual = b.in_order()
    for val in assertions:
        assert actual.next() == val


def test_pre_order():
    """expected nodes in tree"""
    assertions = [5, 4, 3, 2, 8, 7, 43, 22, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    actual = b.pre_order()
    for val in assertions:
        assert actual.next() == val


def test_post_order():
    """expected nodes in tree"""
    assertions = [2, 3, 4, 7, 22, 74, 43, 8, 5]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    actual = b.post_order()
    for val in assertions:
        assert actual.next() == val


def test_breadth_first():
    """expected nodes in tree"""
    assertions = [5, 4, 8, 3, 7, 43, 2, 22, 74]
    b = BinarySearchTree()
    for n in nodes:
        b.insert(n)
    actual = b.breadth_first()
    for val in assertions:
        assert actual.next() == val
