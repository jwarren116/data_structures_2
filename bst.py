#!/usr/bin/env python
from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

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
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val, parent=node)
        elif val > node.val:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val, parent=node)
        else:
            return 'Val already in tree'

    def depth(self):
        """return maximum depth of tree"""
        return self._depth_helper(self.root)

    def balance(self):
        """return integer indicating level of balance based on depth of
        each side"""
        help = self._depth_helper
        return help(self.root.right) - help(self.root.left)

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

    def _find_min(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node

    def _replace_node_in_parent(self, new_value=None):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = new_value
            else:
                self.parent.right = new_value
        if new_value:
            new_value.parent = self.parent

    def remove(self, val):
        if val < self.val:
            self.left.remove(val)
        elif val > self.val:
            self.right.remove(val)
        else:
            if self.left and self.right:
                successor = self.right._find_min()
                self.val = successor.val
                successor.remove(successor.val)
            elif self.left:
                self._replace_node_in_parent(self.left)
            elif self.right:
                self._replace_node_in_parent(self.right)
            else:
                self._replace_node_in_parent(None)

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

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        if not node:
            return
        for val in self._in_order(node.left):
            yield val
        yield node.val
        for val in self._in_order(node.right):
            yield val

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, node):
        if not node:
            return
        yield node.val
        for val in self._pre_order(node.left):
            yield val
        for val in self._pre_order(node.right):
            yield val

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, node):
        if not node:
            return
        for val in self._post_order(node.left):
            yield val
        for val in self._post_order(node.right):
            yield val
        yield node.val

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

    nums = [list(range(0, 251))]

    for num in nums:

        def best_tree(num):
            '''call the recursive method to form the most balanced tree'''
            return best_case(num, 0, len(num) - 1)

        def best_case(num, begin, end):
            if begin > end:
                return None
            mid = (begin + end) // 2
            root = Node(num[mid])
            root.left = best_case(num, begin, mid - 1)
            root.right = best_case(num, mid + 1, end)
            print root.val
            return root

        easy_tree = BinarySearchTree(best_tree(num))
        hard_tree = BinarySearchTree()

        for ints in num:
            hard_tree.insert(ints)

        def hard_find():
            '''find the highest value in the least balanced tree'''
            return hard_tree.contains(num[-1])

        def easy_find():
            '''find the highest value in the most balanced tree'''
            return easy_tree.contains(num[-1])

        print(timeit.timeit('hard_find()',
                            setup='from __main__ import hard_find'))
        print(timeit.timeit('easy_find()',
                            setup='from __main__ import easy_find'))

        dot_graph = hard_tree.get_dot()
        t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
        t.communicate(dot_graph)
