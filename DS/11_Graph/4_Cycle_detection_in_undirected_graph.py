class Solution:

    # Function to detect cycle in an undirected graph.

    # simple dfs program
    # with little tweakin in it
    def dfs(self, parent, src, visited, adj):

        visited[src] = True
        for val in adj[src]:

            if not visited[val]:
                if self.dfs(src, val, visited, adj):
                    return True
            elif parent != val:
                return True
        return False

    def isCycle(self, V, adj):
        visited = [False] * V

        for val in range(V):
            if not visited[val]:
                if self.dfs(-1, val, visited, adj):
                    return True

        return False
