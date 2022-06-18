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


# simple DFS method 
def dfs(src, adjList):

    stack = list()

    visited[src] = True

    stack.append(src)

    while stack:

        cur = stack.pop()

        print(f"{cur}", end=" ")

        for i in adjList[cur]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)


# DFS Recursion
def dfs_recursion(src, adjList):

    visited[src] = True

    print(src, end=" ")
    for val in adjList[src]:
        if not visited[val]:
            dfs_recursion(val, adjList)


# this function making sure if there is any
# node is isolated/not connected
# then iterate through that also
def dfs_util(src, adjList):

    for i in adjList.keys():
        if not visited[i]:
            dfs(i, adjList)

    print()
    for i in adjList.keys():
        if not visited[i]:
            dfs_recursion(i, adjList)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


adjList = g.graph


visited = [False] * (len(adjList) + 1)
dfs_util(2, adjList)

visited = [False] * (len(adjList) + 1)
dfs_recursion(0, adjList)
