"""
Implementing/Playing around w/bt
"""

from operator import add
from typing import Optional

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

    def insert(self, to_insert):
        if to_insert < self.value:
            self.left = self.left.insert(to_insert)
        else:
            self.right = self.right.insert(to_insert)
        return self

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

    def insert(self, to_insert):
        if self.value is None:
            self.value = to_insert
            return self
        elif to_insert < self.value:
            return TreeNode(Leaf(to_insert), Leaf(), self.value)
        else:
            return TreeNode(Leaf(), Leaf(to_insert), self.value)

    def inorder(self, func, merge):
        return self.preorder(func, merge)

    def __len__(self):
        return 1 if self.value else 0


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


bst = Leaf()
bst = bst.insert(3)
bst = bst.insert(4)
bst = bst.insert(1)
bst = bst.insert(10)
bst = bst.insert(-3)
bst.inorder(str, concatenate)
