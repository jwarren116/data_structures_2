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

    def __init__(self, root=None):
        self.root = root
        self.treesize = set()

    def insert(self, val):
        """insert new unique value into tree"""
        self.treesize.add(val)
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
            node_list = []
            for i in self.treesize:
                node_list.append(i)
            new_tree = self.best_tree(node_list)
            self.root = new_tree

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

    def depth(self):
        """return maximum depth of tree"""
        return self._depth_helper(self.root)

    def balance(self):
        """return integer indicating level of balance based on depth of
        each side"""
        left = self._depth_helper(self.root.left)
        right = self._depth_helper(self.root.right)
        return left - right

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

    def _find_min(self, node):
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def _replace_node_in_parent(self, node, new_value=None):
        if node.parent:
            if node == node.parent.left:
                node.parent.left = new_value
            else:
                node.parent.right = new_value
        if new_value:
            new_value.parent = node.parent

    def delete(self, val):
        self.treesize.discard(val)
        # self._delete(val, self.root)
        node_list = []
        for i in self.treesize:
            node_list.append(i)
        new_tree = self.best_tree(node_list)
        self.root = new_tree

    # def _delete(self, val, node):
    #     if val < node.val:
    #         self._delete(val, node.left)
    #     elif val > node.val:
    #         self._delete(val, node.right)
    #     else:
    #         if node.left and node.right:
    #             successor = self._find_min(node.left)
    #             node.val = successor.val
    #             self._delete(successor.val, successor)
    #         elif node.left:
    #             self._replace_node_in_parent(node, node.left)
    #         elif node.right:
    #             self._replace_node_in_parent(node, node.right)
    #         else:
    #             self._replace_node_in_parent(node)

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

    def best_tree(self, num):
        num.sort()
        return self.best_case(num, 0, len(num) - 1)

    def best_case(self, num, begin, end):
        if begin > end:
            return None
        mid = (begin + end) // 2
        root = Node(num[mid])
        root.left = self.best_case(num, begin, mid - 1)
        root.right = self.best_case(num, mid + 1, end)
        return root

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
    # import timeit

    # nums = [list(range(0, 20))]

    # for num in nums:

    #     def best_tree(num):
    #         '''call the recursive method to form the most balanced tree'''
    #         return best_case(num, 0, len(num) - 1)

    #     def best_case(num, begin, end):
    #         if begin > end:
    #             return None
    #         mid = (begin + end) // 2
    #         root = Node(num[mid])
    #         root.left = best_case(num, begin, mid - 1)
    #         root.right = best_case(num, mid + 1, end)
    #         # print root.val
    #         return root

    # easy_tree = BinarySearchTree()
    # easy_tree.insert(5)
    # easy_tree.insert(4)
    # easy_tree.insert(8)
    # easy_tree.insert(3)
    # easy_tree.insert(43)
    # easy_tree.insert(44)
    # easy_tree.insert(127)
    # easy_tree.insert(93)
    # easy_tree.insert(22)
    # easy_tree.insert(7)
    # easy_tree.insert(74)
    # easy_tree.insert(2)

    #     hard_tree = BinarySearchTree()

    #     for ints in num:
    #         hard_tree.insert(ints)

    #     def hard_find():
    #         '''find the highest value in the least balanced tree'''
    #         return hard_tree.contains(num[-1])

    #     def easy_find():
    #         '''find the highest value in the most balanced tree'''
    #         return easy_tree.contains(num[-1])

    #     print(timeit.timeit('hard_find()',
    #                         setup='from __main__ import hard_find'))
    #     print(timeit.timeit('easy_find()',
    #                         setup='from __main__ import easy_find'))

    easy_tree = BinarySearchTree()
    for i in range(40):
        easy_tree.insert(i)

    dot_graph = easy_tree.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)
