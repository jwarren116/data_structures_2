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
        return self.bst_maxdepth(self.root)

    def bst_maxdepth(self, root, depth=0):
        if root is None:
            return depth
        return max(self.bst_maxdepth(root.left, depth + 1),
                   self.bst_maxdepth(root.right, depth + 1))

    def size(self):
        return len(self.treesize)

    def contains(self, val):
        return val in self.treesize
