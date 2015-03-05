#!/usr/bin/env python


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree():

    def __init__(self):
        self.root = None
        self.treesize = set()

    def insert(self, val):
        self.treesize.add(val)
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, node, val):
        if val <= node.val:
            if node.left:
                self.insert_node(node.left, val)
            else:
                node.left = Node(val)
        elif val > node.val:
            if node.right:
                self.insert_node(node.right, val)
            else:
                node.right = Node(val)

    def depth(self):
        return self._depth_helper(self.root)

    def _depth_helper(self, root, depth=0):
        if root is None:
            return depth
        return max(self._depth_helper(root.left, depth + 1),
                   self._depth_helper(root.right, depth + 1))

    def balance(self):
        return self._balance_helper(self.root.left) - self._balance_helper(self.root.right)

    def _balance_helper(self, root, depth=0):
        if root is None:
            return depth
        return max(self._balance_helper(root.left, depth + 1),
                   self._balance_helper(root.right, depth + 1))

    def size(self):
        return len(self.treesize)

    def contains(self, val):
        return val in self.treesize

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.val is None else (
            "\t%s;\n%s\n" % (
                self.val,
                "\n".join(self._get_dot())
            )
        ))

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


if '__name__' == '__main__':
    import random
    import subprocess

    tree = BinarySearchTree()
    tree.insert(20)
    tree.insert(30)
    tree.insert(10)
    tree.insert(15)
    tree.insert(40)

    dot_graph = tree.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)
