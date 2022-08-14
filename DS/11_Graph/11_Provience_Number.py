# https://practice.geeksforgeeks.org/problems/number-of-provinces/1/?page=3&curated[]=8&sortBy=submissions#


class Solution:
    def dfs(self, adj, src, visited):
        visited[src] = True

        # adj[src][i] to check from src to current node == 1(connected or not)
        for i in range(len(adj[src])):
            if not visited[i] and adj[src][i]:
                self.dfs(adj, i, visited)

    # given adjancey matrix
    def numProvinces(self, adj, V):

        ans = 0
        visited = [False] * (V + 1)

        for i in range(V):
            if not visited[i]:
                ans += 1
                self.dfs(adj, i, visited)

        return ans
