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


### Pre-order traversal

visit first the node, then the left branch and finally the right branch

### Post-order traversal

visit the node at last. We first visit the left branch and then the right branch

This is equivalent to perform DFS on the left subtree, then perform DFS on the right
subtree and finally visit the current node


## Binary heaps (min-heaps and max heaps)

A min-heap is a *complete binary tree*, where *each node* is *smaller than it's children*. The root therefore is the 
minimum element in the tree

*Note* Binary heaps can be easily implemented using a list/re-dimensional array. The complexity if u try to use 
linkednodes instead is to keep track of the last rightmost empty element (so we remain it complete)


2 key operations in min-heap: insert and extract_min

### Insert

When we insert, we always start by inserting the element at the bottom. We insert at the rightmost spot
as to maintain the complete tree property

Then, we "fix" the tree by swapping the new element with its parent, until we find an appropriate spot for the element
We bubble up the min

This operation takes O(log N) where N is the amount of elements in the heap

## Extract minimum

Finding the minimum is easy because it's the root. What we need to take into consideration is 
re-balancing the heap so we mantain the heap property (all childrens are smaller than the root)

How do we do this? We grab the right-most element (last element of the heap) and we bubble it down
until we find it's position by swapping it with other nodes always fulfilling the heap invariant.

Do we swap it w/left or right child? Depends on the value, important thing is to keep the invariant

## Building a heap from a list

Note heapifying or building a heap from a list, assumming complete heap, takes O(N) and not O(N log N). See the following links for a better explanation:

1. Explanation by Tim Peters [here](https://stackoverflow.com/questions/51735692/python-heapify-time-complexity)
2. Heapify implementation in Python [here](https://github.com/python/cpython/blob/3.13/Lib/heapq.py#L260)


*Important to remember:* Inserting n elements into a heap takes O(N * log N) while heapifying a list takes O(N) 


## Implementation (coming from Algorithms 4th edition)

We implement it using an array. Why? Because complete trees allow us to use a compact array 
representation that does not involve explicit links

*Note* If you want to implement a binary heap using a linked representation, you need to keep
track of the parent so you can travel up and down the tree.

In a heap, the parent of the node in position k is in position [k//2] and, conversely, the two
children of the node in position k are in position 2k and 2k + 1

This means that for moving up (travelling to the parent), we do k//2 while for moving down we 
do either 2*k or 2*k + 1


*Representation* An array pq of length N + 1 where pq[0] is unused and the heap goes
from pq[1] to pq[N] (We avoid using the first element so the operations for moving to the childrens is easier, otherwise, if you want to use pq[0] then to get to the childrens u need to do 2k + 1 & 2*k + 2, because it's 0 based-index)


*2 types of operations*
- Decrease priority: We decrease the priority which means that we need to swim up a node
- Increase priority: We increate the priority which means that we need to swim down the node

swim down = sink, swim up = swim = reheapify

*Note* The above is inverted for max-heap



## Tries (Prefix Trees)

It comes up a lot in interview questions!

A trie is a variant of an n-ary tree in which characters are stored at each node. Each path
down the tree may represent a word

The * nodes (sometimes called "null nodes") are often used to indicate complete words. For example,
the fact there is a * node under MANY indicates that MANY is a complete word. The existance of the MA
path indicates there are words that start with MA.

Actual implementation of these * nodes might be a special type of child (such as TerminatingTrieNode, 
which inherits from TrieNode). Or we could use just a boolean flag termiantes withing the "parent" node.

A node in a trie could have anyware from 1 through ALPHATEB_SIZE + 1 children ( or 0, through ALPHABET_SIZE
if a boolean flag is used instead of a * node)


*Note*: While a hash table can quickly look up wether a string is a valid word, it cannot tell us if a string
is a prefix of any valid words. A trie can do this very quickly.


*Note 2*: How quickly? A trie can check if a string is a valid prefix in O(K), where K is the length of the string.
Note that a hash table ALSO TAKES O(K) for accessing the value of a string s where len(s) = K. Why? Because you 
need to read the whole string for getting it's hash! And this takes O(K) --> Do u really need to read the whole string?

See `tries.py`
