A tree is nothing more than a special type of graph

*Note* Easiest way to implement the tree structure:

```python
class TreeNode:
	def __init__(self, value=None, childrens=None):
		self.value = value
		self.childrens = childrens if childrens else []
```

In rare cases defining the tree class makes sense:

```python
class Tree:
	def __init__(self, root: Optional[TreeNode] = None):
		self.root = root
```

*Remember* A tree by definition doesn't have a cycle


Of course the TreeNode definition I gave above is generic, meant for trees with variable number
of childrens. Reality is that we will usuay use binary or ternary trees


## Binary tree vs binary search tree

A binary search tree is a binary tree in which every node fits a specific ordering which is:

`all left leafes <= n (root node) < all right leafs`

The above must be true for every node in the tree

*Note regarding duplicates* There are some definitions where binary trees can have duplicates and
some definitions where this is not allowed. This is something that must be clarify during the interview


*Important* Always ask in the interview if when talking about binary trees we are talking about BST or just
plain BT


## Balanced vs unbalanced

While many trees are balanced, not all are. Ask your interviewer for clarification

*Note* Balancing a tree does not mean the left and right subtrees are exactly the same size!
(The above is called "perfect binary tree"). Our goal is to keep a tree "as balance as possible"
so we can keep the O(log N) runtime when inserting and finding elements

2 types of balanced trees are: 1) Red-black trees and AVL trees.


## Properties of BT

### Complete Binary Tree

Is a binary tree in which every level of the tree is fully filled, except for perhaps the 
last level. To the extent that the last level is filled, it is filled left to right


### Full binary tree

Each node has either zero or two childrens. That is, no node has only 1 child

### Perfect binary tree (usually doesn't happen, neither in interviews nor in real life)

Both full and complete at the same time


## Binary Tree Traversal

How do we traverse the graph? we have 3 ways

### In-order traversal

"visit" the left branch, then the current node and finally the right branch

*Note* If we do inorder traversal in a BST, then we are visiting the nodes in ascending order :)
Why? Because by favoring resolving the left subtree at each node, we are always moving toward
the smallest value available and returning the inorder successor
