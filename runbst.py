from bst import BinarySearchTree


b = BinarySearchTree()

b.insert(5)
b.insert(4)
b.insert(7)
b.insert(10)
b.insert(8)
b.insert(3)
b.insert(2)
b.insert(1)
b.insert(.5)

print b.treesize
print b.root.val
print b.depth()
