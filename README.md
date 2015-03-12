# Data Structures 2
## ft. James and Nick

*March 4th, 2015* - Added a Binary Search Tree data structure. The tree has nodes, and every node can have two children.
                  Each child of a node is sorted the following way: if the new node is greater than the current node,
                  add it to the right, if it's left, add it to the left. Otherwise, ignore it if they are the same. The
                  following methods were implemented:

                  1. Node Class and Tree Class, both are the base structure for the BST.
                  2. insert(node): Adds a node with a given value to the tree.
                  3. depth(): Returns the max depth of the tree, i.e number of levels down it goes.
                  4. balace(): Looks at the max depth of both sides and returns which is deeper.
                  5. size(): Returns the number of nodes in the tree.
                  6. contains(node): Returns a boolean for if the node is in the tree or not

*March 5th, 2015* - Added 4 different methods of traversal for the BST. These will each be a generator object
                    that yields the next number to be produced in that traversal method. Has the following modes:

                  1. beadth_first_traversal(): Yields nodes in the order top down, left to right.
                  2. in_order(): Delves left first as far as possible, then moves up, then to the right.
                  3. pre_order(): Starting at the root, return each value moving down. Then each moving up to the right.
                  4. post_order(): Similar to in_order, but returns the root at the end after the right branch left facing nodes.

*March 9th, 2015* - Added deletion to our Search Tree. Our delete() function takes the value to be deleted, and returns None in all cases.

*March 11th, 2015* - Added rebalancing of our Search Tree when nodes are inserted or deleted.