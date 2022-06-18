from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def shortest_path(self, src):

        q = list()

        visited = [False] * (max(self.graph) + 1)

        q.append([src, 0])
        print(f"Distance from {src} to Node  ")
        while q:

            cur = q.pop(0)

            print(f"{cur[0]}  is {cur[1]}")

            for val in self.graph[cur[0]]:
                if not visited[cur[0]]:
                    visited[cur[0]] = True
                    q.append([val, cur[1] + 1])


# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


g.shortest_path(2)
