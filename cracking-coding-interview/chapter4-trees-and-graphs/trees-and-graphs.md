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

TODO -> IMPLEMENT A TRY


## Graphs

A tree is a type of graph without cycles.

Graph is a collection of nodes and edges. Graphs can be directed or undirected. 
Directed => edge goes 1 way
Undirected => edge goes 2 ways

- The graph might consist of multiple isolated subgraphs. If there's a path between 
every pair of vertices then you are in a connected component
- The graph can also have cycles. Acyclic graph then means no cycles

## Summary on graph problems:

- Single source shortest paths: O(|V| + |E|) bfs (I need to iterate over all nodes, 
even those that I cannot reach in order to set a value for the path)
*Note* In this problem, distance = #(edges) => edge = 1 
- Single source reachability: O(|E|), dfs
- Connected components: O(|V| + |E|), dfs
- Topological sort (only valid for a DAG): O(|V| + |E|), dfs + push elements in a stack

*Note* Linear time in graphs is O(|V| + |E|)


## Representing a graph

### Adjacency List

Most common way. Every vertex stores a list of adjacent vertices. 
In an undirected graph, (a, b) edge will be stored twice (once in a and another 
time in b)

```
class Graph:
	nodes: list[list[int]] # if we represent a vertex as an integer
```

We can also define Node class

```
class Graph:
	nodes: list[Node]
	
class Node:
	name: str | int
	children: list[Node]
```

### Adjacency Matrix

NxN matrix m (N = number of nodes), where m[i][j] == True <--> there is an edge from i to j. If we are in
an undirected graph, then it means that if m[i][j] == True <---> m[j][i] == True (the matrix will be symmetric)


*Note* If you care more on given an edge, it's neighbours, then an adjacency list structure may be more convenient.
On the contrary, if you care more about edges, then prefer the adjacency matrix


## Graph search


### DFS - Depth first search

If we "insert" elements at the beginning of the list, then we are 
using the list as a stack. This means that we are pushing childrens
on top of the stack. Because of this, every time we pick the next 
first element, we will be picking always a new children of different
level than the previous one (because we always push on top). This is
why this is the depth first search algorithm

```
def dfs(root):
	visited = []
	to_visit = [root]
	curr = visisted.pop()
	visited.append(curr)
	while curr is not None:
		for each node in curr.children:
			if node not in visited:
				to_visit.insert(0, node)
		visited.append(curr)
		curr = to_visit.remove()

```

Given that we are using a stack, we could just use the memory stack of
calls of functions and do the dfs method recursive:

```
def dfs(root: Node, visit: Callable[[Node], int]):
	if root is None:
		return None
		
	curr = root
	while curr is not None:
		visit(curr)
		for child in curr.children:
			if child.visited == False:
				child.visited = True
				visit(child)
				dfs(child, visit)
		curr = next_not_visited_node # Visit the next connected component
```


### BFS - Breadth first search

If we append childrens into the visited list, then we are using 
the visited as a queue. By doing this, we first visit all childrens 
of the same level before moving to the next level

```
def bfs(root):
	visited = []
	to_visit = [root]
	curr = visisted.pop()
	visited.append(curr)
	while curr is not None:
		to_visit.extend([node for node in curr.children if node not in visited]) # put childrens last
		visited.append(curr)
		curr = to_visit.remove()

```


### Considerations

- If we want to find the shortest path, bfs it's better. DFS will find a path, but not necessarily the 
shortest path


### Reviewing graph theory

*Directed graph:* 
Bound: |E| <= 2(|v| 2) = O(|v|^2) (combinatory number)
The 2 comes from the fact that we care about ordering! It's not the
same counting from v to w than w to v

*Undirected:* Bound: |E| <= (|v| 2) = O(|v|^2)

Why the above? Because it helps us to understand

1) Reasoning about the complexity of the algorithm we are working at
2) If we know more about the graph, then we can actually know if it's
better to work on edges or on vertices (Example: Think of a sparse 
graph, where sparse graph means a graph where the number of edges is
way smaller than the number of vertices)


*Concepts:*
- out degree -> number of edges that go out of the vertex (|Aj-(v)|)
- in degree -> number of edges that come in the vertex (|Aj+(v)|)
- adjacency list out (Aj-(v)) -> { w belong V / (v, w) belong E }
- adjacency list in (Aj+(v)) -> { w belong V / (w, v) belong E }
- Sum(u belong V) deg+(u) = The sum of all out degrees of all my vertices = 
{
- 2|E| if undirected graph
- |E| if directed graph
}
- Level set = Lk = {v belong V / d(s, v) = k} # this is, all vertices that are at their shortest distance k of v

Why do we care about the above concepts? Because in our graph algorithms we usually
iterate over: 1) the out degree of a vertex, or 2) The edges that go into a vertex, 
and so on


## Graph representation

One that I didn't mention above is the edge list. Not so useful, but okay, it exists


## Model graph problems regarding paths

1. Single pair reachability, (G, s, t): Is there a path between s and t?
2. Shortest path, (G, s, t): What is the shortest path between s and t?
3. Single source shorest path, (G, s): Give me all the shortest path between s and all v belong V


*Notes* 
1. Shortest path is a tree, cycles don't make sense :)
2. We need O(V) space to store the shortest path tree. This is, per each node, store
the previous edge that belongs to the shortest path
3. Shortest path property is greedy. This means, in every step taking the smallest 
edge is the best global option

Another note: if 1 edge is added to the graph, then ALL the shortest paths need to be
recalculated :)


### Shortest Path problem from edg

Use BFS. We can construct the algorithm recursively by considering levels. So per each level_i, we build level_i+1 inductively using the previous level. Per building the path from whatever node w to v, we recursively use our path structure that will contain per each vertex, the node that it got us to the vertex

*Note* BFS runs in O(|V| + |E|)


### Single source reachability problem

Problem statement: What are all the nodes of the graph I can reach from starting on this node?


Use DFS :)

```
def dfs(v):
	visited = {}
	for w in v.neighbors():
		if w not in visited:
			visited.add(w)
			dfs(w)
```

Runtime: O(|E|) -> I never reach a vertex that is not reachable


## Full DFS

It's just applying dfs over all vertices. Useful for finding connected components

```
def fulldfs(g: Graph):
	visited = {}
	for v in g.nodes():
		if v not in visited:
			visited.add(v)
			dfs(v)
```

The above algorithm takes O(|V| + |E|) because each edg is touch no more than one time
and then no vertex is visited more than 1 time because we ask `v not in visited`


## Definitions

(Airflow as application) *Directed Acyclic graph (DAG):*

Example of a DAG: A tree!

Important application: Assigning tasks and ordering them corresponding with its dependency


*Topological Order:* Ordering f over vertices where f(u) < f(v) for all (u, v) in E 
(If I have an edg between u and v, then f(u) < f(v) )

*Finishing order:* Order in which a full DFS finishes visiting each vertex


If we have a reverse finishing order, then we have a topological order on our graph

G DAG => reverse of finishing order is a topological order


### Problem Cycle detection

Given a directed graph, Does it exist a cycle in it?

We can just apply dfs on the DAG and see if we get a topological order. If we don't have it, then
it's not a DAG

*Another property:* G contains cycle => Full DFS traverse edge v -> ancestor of v


## Topological order in a DAG

(Section coming from coursera algorithms part2)

*Goal*: Given a set of tasks to be completed with precedence constraints, in which order
should we schedule the tasks?

*Model:* vertex = task; edge = precedence constraint

What do we want? A "feasible schedule", which is, a linear order of the nodes that respect the precedences
"Draw" the graph such that all edges point upwards

*Note:* A topological sort only works in a DAG, Directed *Acyclic* graph
If u have a cycle, then the problem is not solvable

*Note 2:* Topological sort = topological order, i.e.: Draw the graph such that all edges point upwards

*Solution:* Use DFS

So first thing to check in topological sort:
if cycle in DAG:
	return "No topological order"

Applications: 
1. Scheduling!
2. Ordering a course curricula
3. Cycle detection in inheritance
4. Microsoft Excel! 


## Weighted directed graphs

Now edges have weight!, G, w: E -> Z (integers)

Given e = (u, v), w(e) = w(u, v)

### How do we represent weights in a graph?

1. Add the weight in the adjacency list -> Means, instead of just the edge, we store the pair (v,weight)
2. Separate set data structure mapping edges to weights


*Important* We can query weight in O(1)

So given weights, we can now define:
1. Weighted Paths -> Just the sum of weight of edges in the path
2. Shortest (weighted) path -> Min weight path

*Note* If we have negative edges, then things get funnier :D
Why? Because if you have a cycle that sums a negative value, then 
you don't have a minimum path bc u can always iterate over and 
over again that cycle to get a smaller value

Example:

a -(-1)-> b -(-1)--> a


*Moral* Take care of negative-weight cycles!


### Calculating shortest path in asymptotically bounded weighted graph

We already know that we can apply BFS to solve the shortest path problem in 
an directed graph without weights.

If we have a directed graph with weights, and the sum of all weights < K where K is constant, 
we could reduce the problem of finding the weighted shortest path to BFS by observing the following:

If we have a weight such as this: a --(4)-> b (meaning, w(a, b) = 4), we could re-consider our graph
to be -> a -1-> a1 -1-> a2 -1-> a3 --1> b 

What did we do? We created 4 edges of weight 1 for that edge of weight 4! In this way, we can always
reduce our G=(V, E) to a G'=(W, E') where #(V) < #(W) + some constant factor (because weights are bounded)


## Sumary

| Graph   | Weights      | Name           | Running Time      |
| General | Unweighted   | BFS            | O(V + E)          |
| DAG     | ANY          | DAG Relaxation | O(V + E)          |
| General | Any          | Bellman-Ford   | O(V* E)           |
| General | Non-negative | Dijkstra       | O(V * log(V + E)) |
