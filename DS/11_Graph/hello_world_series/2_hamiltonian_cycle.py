# https://practice.geeksforgeeks.org/problems/euler-circuit-and-path/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Graph&curated[]=7&sortBy=submissions


# this is also Knowns as Euler Circuit

# same logic as Hamilonian path
class Solution:
    ans = 0

    def dfs(self, src, visited, graph, n, psf, oz_src):

        if psf == n - 1:
            self.ans = 1

            circuit = False
            # we only checking that the new src
            # having original_src(oz_src) as neighbour
            # if yes then it makes a complete cycle/circuit
            for adj in graph[src]:
                if adj == oz_src:
                    circuit = True
                    break

            if circuit:
                self.ans = 2

        visited.add(src)

        for adj in graph[src]:
            if adj not in visited:
                self.dfs(adj, visited, graph, n, psf + 1, oz_src)

        visited.remove(src)

    def isEularCircuitExist(self, V, adj):

        """
        Simple and crisp solution:

        If no. of odd degree nodes = 0  → Euler circuit

        If no. of odd degree nodes = 2  → Euler path

        In all other cases neither Euler circuit nor Euler path
        """

        odd = 0
        for i in range(V):
            if len(adj[i]) & 1:
                odd += 1
        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        else:
            return 0

        # ------------------- TLE -------------------------
        visited = set()
        for i in range(V):
            self.dfs(i, visited, adj, V, 0, i)
            if self.ans == 2:
                return self.ans
        return self.ans
