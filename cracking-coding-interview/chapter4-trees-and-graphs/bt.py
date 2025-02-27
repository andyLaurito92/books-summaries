"""
Implementing/Playing around w/bt
"""

class TreeNode:
    def __init__(self, left, right, value):
        if not issubclass(type(left), TreeNode):
            raise ValueError("Left tree must be a binary tree")
        elif not issubclass(type(right), TreeNode):
            raise ValueError("Right tree must be a binary tree")

        self.left = left
        self.right = right
        self.value = value

    def inorder(self, func, merge):
        return merge(
            self.left.inorder(func, merge),
            func(self.value),
            self.right.inorder(func, merge)
        )

    def preorder(self, func, merge):
        return merge(
            func(self.value),
            self.left.preorder(func, merge),
            self.right.preorder(func, merge)
        )

    def postorder(self, func, merge):
        return merge(
            self.left.postorder(func, merge),
            self.right.postorder(func, merge),
            func(self.value)
            )

    def __len__(self):
        return 1 + max(len(self.left), len(self.right))


class Leaf(TreeNode):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self, func, merge):
        return func(self.value) if self.value else ""

    def postorder(self, func, merge):
        return self.preorder(func, merge)

    
    def inorder(self, func, merge):
        return self.preorder(func, merge)

    def __len__(self):
        return 1 if self.value else 0


class BinarySearchTreeNode(TreeNode):
    def insert(self, to_insert):
        if to_insert < self.value:
            self.left = self.left.insert(to_insert)
        else:
            self.right = self.right.insert(to_insert)
        return self


class BinarySearchLeaf(Leaf):
    def insert(self, to_insert):
        if self.value is None:
            self.value = to_insert
            return self
        elif to_insert < self.value:
            return BinarySearchTreeNode(
                BinarySearchLeaf(to_insert),
                BinarySearchLeaf(),
                self.value)
        else:
            return BinarySearchTreeNode(
                BinarySearchLeaf(),
                BinarySearchLeaf(to_insert),
                self.value)


# The easiest way to implement this min/max heap is by
# using an array. If you want to implement it using a
# type of linked list, you can try to keep the size of
# the heap and traverse the tree by using the knowledge
# of how many items u have. Because it is a complete tree
# then we have a guarantee on where the last element should be
class MinHeapTreeNode(TreeNode):
    def insert(self, to_insert):
        # If I'm a tree node of a min-heap, then
        # 2 options: 1) right branch is empty, 2)
        # both branches are already fulled! => new level
        # Note: If left branch is None => right branch is None
        # => I'm a leaf! It cannot happen otherwise, because then
        # I wouldn't have a complete tree
        if self.right is None:
            self.right = MinHeapTreeNode(
                MinHeapLeaf(),
                MinHeapLeaf(),
                to_insert)
        else:
            # both branches are complete!, try
            # left branch
            self.left.insert(to_insert)
        
    

# class MinHeapLeaf(Leaf):
#     def insert(self, to_insert):
#         if self.value is None:
#             self.value = to_insert
#         elif:
#             return MinHeapTreeNode(
#                 MinHeapLeaf(to_insert),
#                 MinHeapLeaf(),
#                 self.value)
#         self.rebalance()

#     def rebalance(self):
#         # A leaf cannot break the min-heap invariant
#         return
                

mytree = (
    TreeNode(
        TreeNode(
            Leaf(1),
            TreeNode(Leaf(4), Leaf(7), 6),
            3),
        TreeNode(
            Leaf(),
            TreeNode(Leaf(13), Leaf(), 14),
            10),
        8
    )
)

concatenate = lambda x, y, z: f"{x} {y} {z}"

mytree.inorder(str, concatenate)

mytree.preorder(str, concatenate)

mytree.postorder(str, concatenate)


bst = BinarySearchLeaf()
bst = bst.insert(3)
bst = bst.insert(4)
bst = bst.insert(1)
bst = bst.insert(10)
bst = bst.insert(-3)
bst.inorder(str, concatenate)
