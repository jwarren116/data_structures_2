#!/usr/bin/env python
from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = None
        self.right = None

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.val, self.left.val)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.val, self.right.val)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.treesize = set()

    def insert(self, val):
        """insert new unique value into tree"""
        self.treesize.add(val)
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val <= node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)
        elif val > node.val:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)

    def depth(self):
        """return maximum depth of tree"""
        return self._depth_helper(self.root)

    def balance(self):
        """return integer indicating level of balance based on depth of
        each side"""
        return self._depth_helper(self.root.right) -\
            self._depth_helper(self.root.left)

    def _depth_helper(self, root, depth=0):
        if root is None:
            return depth
        return max(self._depth_helper(root.left, depth + 1),
                   self._depth_helper(root.right, depth + 1))

    def size(self):
        """return number of nodes in tree"""
        return len(self.treesize)

    def contains(self, val):
        """return True if value found in tree, False if not"""
        return val in self.treesize

    def breadth_first(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            yield node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.root.val is None else (
            "\t%s;\n%s\n" % (
                self.root.val,
                "\n".join(self.root._get_dot())
            )
        ))


if __name__ == '__main__':
    import random
    import subprocess
    import timeit

    tree = BinarySearchTree()
    nums = [i for i in range(101)]
    for i in nums:
            tree.insert(i)

    def hard_find():
        tree.contains(100)

    def easy_find():
        tree.contains(1)

    print(timeit.timeit('hard_find()', setup='from __main__ import hard_find'))
    print(timeit.timeit('easy_find()', setup='from __main__ import easy_find'))

    dot_graph = tree.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)
