from collections import defaultdict

visited = list()


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


# simple BFS method for doing Level-Order traversal
def bfs(src, adjList):

    q = list()

    visited[src] = True

    q.append(src)

    while q:

        cur = q.pop(0)

        print(f"{cur}", end=" ")

        for i in adjList[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


# this function making sure if there is any
# node is isolated/not connected
# then iterate through that also
def bfs_util(src, adjList):

    for i in adjList.keys():
        if not visited[i]:
            bfs(i, adjList)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


adjList = g.graph


visited = [False] * (len(adjList) + 1)
bfs_util(2, adjList)
