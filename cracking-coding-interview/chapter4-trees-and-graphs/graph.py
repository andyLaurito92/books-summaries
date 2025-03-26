# We assume simple graph, meaning, neighbors don't repeat
class Graph:
    nodes: list[str]

    def __init__(self):
        self.nodes = {}

    def addVertices(self, nodes: list[str]):
        for node in nodes:
            self.addVertex(node)

    def addEdges(self, edges: list[(str, str)]):
        for v, w in edges:
            self.addNeighbor(v, w)

    def addVertex(self, node: str):
        self.nodes[node] = set()

    def addNeighbor(self, node: str, neighbor: str):
        self.nodes[node].add(neighbor)
        
    def bfs(self, func: callable):
        visited = set()

        if len(self.nodes) == 0:
            return # Nothing to do

        for vertex in self.nodes:
            if vertex not in visited:
                visited.add(vertex)
                func(vertex)
                for neighbor in self.nodes[vertex]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        func(neighbor)

    # visited = {}, start = 1
    # visited = {1}, start = 1, vertex = 2, 2 not in visited, dfs(2, func, {1})
    # visited = {1, 2}, start = 2, vertex = 3, 3 not in visited, dfs(3, func, {1, 2}
    # visited = {1, 2, 3}, start = 3, vertex = 6, 6 not in visited , dfs(6, func, {1, 2, 3})
    # visited = {1, 2, 3, 6}, start = 6, no vertex, mystack.append(6) =[6]
    # visited = {1, 2, 3, 6}, start = 3, no vertex, mystack.append(3) = [6, 3]
    def dfs(self, start: str, func: callable,
            visited: set[str] = None) -> set[str]:

        visited = set() if visited is None else visited
        visited.add(start)
        for vertex in self.nodes[start]:
            if vertex not in visited:
                self.dfs(vertex, func, visited)
        func(start)
        return visited

    def topologicalsort(self) -> str:
        mystack = []

        def stack(vertex: str):
            mystack.append(vertex)

        visited = set()
        for vertex in self.nodes:
            if vertex not in visited:
                vertices_visited = self.dfs(vertex, stack, visited)
                visited = visited.union(vertices_visited)

        return ' '.join(reversed(mystack))
          

    def shortest_path_tree(self, v: str):
        """
        Get the shortest path between v and all other nodes
        """
        path = {v: ('-', 0)}
        to_visit = [(v, 0)]
        visited = set()
        while len(to_visit) != 0:
            curr, curr_level = to_visit.pop()
            visited.add(curr)
            for vertex in self.nodes[curr]:
                if vertex not in visited:
                    to_visit.append((vertex, curr_level + 1))
                if path.get(vertex, None) is None:
                    path[vertex] = (curr, curr_level + 1)

        for vertex in self.nodes:
            if vertex not in visited and vertex != v:
                path[vertex] = -1

        return path

    def __str__(self):
        nodes = []
        self.bfs(lambda x: nodes.append(str(x)))
        return ' '.join(nodes)


# We represent a directed graph 
g = Graph()

v3 = '3'
v2 = '2'
v1 = '1'

vertices = [v1, v2, v3]
edges = [(v1, v3), (v2, v3)]

g.addVertices(vertices)
g.addEdges(edges)
str(g)
g.shortest_path_tree(v1)


g2 = Graph()

v4 = '4'
v5 = '5'
v6 = '6'

"""
 V1 → V2 → V3  
       ↘  ↗  │  
         V5  │  
       ↗  │  ↓  
       V4  → V6  
"""

edges = [(v1, v2), (v2, v3), (v3, v5), (v2, v5), (v1, v3), (v4, v5), (v5, v6)]

g2.addVertices([v1, v2, v3, v4, v5, v6])
g2.addEdges(edges)

print("Shortest path from v1 ", g2.shortest_path_tree(v1))
print("Shortest path from v2 ", g2.shortest_path_tree(v2))
print("Shortest path from v6 ", g2.shortest_path_tree(v6))


g2.topologicalsort()
