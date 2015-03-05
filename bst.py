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
        return self._balance_helper_left(self.root.left) - self._balance_helper_right(self.root.right)

    def _balance_helper_right(self, root, depth=0):
        if root is None:
            return depth
        return max(self._balance_helper_right(root.left, depth + 1),
                   self._balance_helper_right(root.right, depth + 1))

    def _balance_helper_left(self, root, depth=0):
        if root is None:
            return depth
        return max(self._balance_helper_left(root.left, depth + 1),
                   self._balance_helper_left(root.right, depth + 1))

    def size(self):
        return len(self.treesize)

    def contains(self, val):
        return val in self.treesize
