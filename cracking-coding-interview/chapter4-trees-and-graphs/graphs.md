## Graphs

A tree is a type of graph without cycles.

Graph is a collection of nodes and edges. Graphs can be directed or undirected. 
Directed => edge goes 1 way
Undirected => edge goes 2 ways

- The graph might consist of multiple isolated subgraphs. If there's a path between 
every pair of vertices then you are in a connected component
- The graph can also have cycles. Acyclic graph then means no cycles
- The distance between vertices v and w in a graph (distance(v,w)) it's defined as the *shortest distance* between u and v

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


## Property Graph connected

If a graph is connected => every vertex is adjacent to at least 1 edge. But an edge is
adjacent to 2 vertices by definition => 2|V| <= |E| => |V| <= |E|/2

## Shortest-path trees 
For weighted, only need parent-pointers for v with finite shortest path distance

Given an array of distances, this is, distance[v] contains the distance from s to v.
This algorithm can be used for creating the parentpointer structure from the distances array

```
parentpointer = [None] * length(g.nodes)
distance # structure that contains the lengths of the paths between s and all vertices in the graph

for v in g.nodes:
	if distance[v] != -1: # Distance is not infinity
		for w in g.adjacency(v):
			if parenpointer[w] is None and distance[w] == distance[v] + w(v, w):
				# it exist a shortest path that uses (u, v)! There might be more than
				# 1 shortest path, but surely this is a shortest path
				parentpointer[w] = v 
```

The above algorithm is O(|V| + |E|) which is linear time (for graphs). Meaning that from now onwards, 
we don't really care about calculating parentpointer given that we can get them from the shortest distance


## DAG relaxation

Mantain distances(s, v) = -1
Calculate triangle inequality over vertices

*Triangle inequality*

It always needs to happen that distance(s, v) <= distance(s, u) + w(u, v), if (u, v) belongs to edges. 
So it means that if we have distance(s, v) > distance(s, u) + w(u, v) then it means that we have a shortest path
from s to v passing through u

"Relax" means lowering d(s,v) by using u

Algorithm:

```
distance = [infinity] * leng(V)
for s in V:
	distance[s] = 0
	
for v in g.topologicalsort(): # Why has to be in topological sorting order?
	for w in g.adjacents(v):
		if distance[v] > distance[w] + w(v, w):
			distance[v] = distance[w] + w(v, w) # relax edge
	

```
