"""
Network problems

Measurements on graphs. Radius of a graph (is a min-max problem)

Given an undirected graph G=(V,E) (can be a network). Given v, we define
eccentric as ecc(v) = w <--> for all u in V, max(distance(v, u)) = w.
It's the max distance that I have from a vertex v to some other vertex in the graph

Given the above, we can define the radius as R(G) = min(eccentric(u)) of all u in V 

Why does the above work? Think on a circle, and think on each point inside the circle
as a node in the graph. We can define eccentric for each of these new points in the circle
as the longest distance to one of the sides.

Between all these max distances, which would be the minimum of all of them? The center!

1. Give an algorithm to compute the radius of a graph
2. Give an algorithm for approximating the radius of a graph really quick :)
"""

"""
We know how to calculate distances by using dfs
"""

Node = int

from collections import defaultdict, deque


"""
1. There are no repeated edges between 2 nodes in a graph because there's no difference.
This makes sense to represent when we have weight edges :)

2. Because of the above, we count distance as number of edges between graph v and w
"""
class DGraph: # Directed graph
    @classmethod
    def createFrom(clss, vertices: list[tuple[Node, Node]]) -> 'Graph':
        graph = DGraph(len(vertices))
        for v, w in vertices:
            graph.addEdge(v, w)

        return graph

    def __init__(self, numvertices: int):
        self.adjacencymap = [set() for _ in range(numvertices)]

    def addEdge(self, v: Node, w: Node) -> None:
        self.adjacencymap[v].add(w)


    def bfs(self, v: Node, f: callable) -> None:
        tovisit = deque()
        tovisit.append((v, 0))
        visited = set()
        while len(tovisit) > 0:
            curr, level = tovisit.pop()
            if curr in visited:
                continue
            f(curr, level)
            visited.add(curr)
            for w in self.adjacencymap[curr]:
                tovisit.append((w, level+1))

    def distancesFrom(self, v: Node) -> list[int]:
        distances = [-1] * len(self.adjacencymap)

        def relaxation(w: Node, distance: int):
            if distances[w] == -1:
                distances[w] = distance
            elif distances[w] > distance:
                distances[w] = distance

        self.bfs(v, relaxation)

        return distances


    def eccentric(self, v: Node) -> Node:
        """
        Returns the eccentric node, this is, the node
        whose distance is the max between all nodes
        in the graph
        """
        distances = self.distancesFrom(v)
        max_distance = distances[0]
        eccentric = 0
        for node, distance in enumerate(distances):
            if max_distance < distance:
                eccentric = node
                max_distance = distance

        return eccentric
                 

g = DGraph.createFrom(
    [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 2),
        (4, 5),
        (0, 3),
        (1, 5)
     ]
)


print(g.distancesFrom(1))
print(g.eccentric(1))
