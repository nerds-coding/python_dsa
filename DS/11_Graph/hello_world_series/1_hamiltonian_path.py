# https://practice.geeksforgeeks.org/problems/hamiltonian-path2522/1


class Solution:
    # to simplify the capturing the answer
    # I made and variable Global
    ans = False

    def dfs(self, src, visited, graph, n, psf):
        # psf -> point so far
        # to count till how many edges we have met
        # all are unique
        # n-1 bcz when we enter the dfs we are counting
        # the src after this if conditions
        if psf == n - 1:
            self.ans = True
            return
        visited.add(src)

        for adj in graph[src]:
            if adj not in visited:
                # if this condition is true
                # psf + 1, bcz we are now encountering the unique edges
                self.dfs(adj, visited, graph, n, psf + 1)

        # removing the src bcz
        # we have to explore all the path
        # not only the unique path
        # so trying all the path from given src
        visited.remove(src)

    def check(self, N, M, Edges):

        graph = dict()

        # making graph
        for ed in Edges:
            graph[ed[0]] = [ed[1]] + graph.get(ed[0], [])
            graph[ed[1]] = [ed[0]] + graph.get(ed[1], [])

        # doing this in loop
        # bcz we want to explore from all the possible edges
        # such if we found the route where we can visit all the
        # vertices atleast once
        for i in range(1, N + 1):
            visited = set()
            self.dfs(i, visited, graph, N, 0)
            if self.ans:
                return self.ans
        return self.ans
