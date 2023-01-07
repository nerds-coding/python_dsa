# https://practice.geeksforgeeks.org/problems/water-connection-problem5822/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Graph&curated[]=7&sortBy=submissions


class Solution:
    def fill_stack(self, src, visited, stack, graph):
        visited[src] = True

        for adj in graph[src]:
            if not visited[adj]:
                self.fill_stack(adj, visited, stack, graph)

        stack.append(src)

    def dfs(self, src, visited, graph, ans):
        visited[src] = True
        for adj in graph[src]:
            if not visited[adj]:
                self.dfs(adj, visited, graph, ans)

        ans.append(src)

    def solve(self, n, p, a, b, d):

        visited = [False] * (n + 1)
        stack = list()
        graph = {i: [] for i in range(1, n + 1)}

        for i in range(p):
            graph[a[i]].append(b[i])

        for i in range(1, n + 1):
            if not visited[i]:
                self.fill_stack(i, visited, stack, graph)

        visited = [False] * (n + 1)

        res = list()
        while stack:
            ans = list()
            adj = stack.pop()
            if not visited[adj]:
                self.dfs(adj, visited, graph, ans)
                res.append(ans)

        final = []
        weight = {a[i]: d[i] for i in range(len(d))}
        for val in res:
            final.append(
                [val[-1], val[0], min([weight.get(i, float("inf")) for i in val])]
            )
        final = sorted(final, key=lambda x: x[0])
        print(final)


n = 9
p = 6
a = [7, 5, 4, 2, 9, 3]
b = [4, 9, 6, 8, 7, 1]
d = [98, 72, 10, 22, 17, 66]

Solution().solve(n, p, a, b, d)
