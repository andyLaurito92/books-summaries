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
