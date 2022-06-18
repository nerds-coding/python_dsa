# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1#


class Solution:
    def dfs(self, src, adj, visited, path_visited):
        visited[src] = True
        path_visited[src] = True

        for val in adj[src]:
            if not visited[val]:
                if self.dfs(val, adj, visited, path_visited):
                    return True
            elif path_visited[val]:
                return True

        path_visited[src] = False
        return False

    def isCyclic(self, V, adj):

        visited = [False] * V
        path_visited = [False] * V

        for i in range(V):
            if self.dfs(i, adj, visited, path_visited):
                return True

        return False
