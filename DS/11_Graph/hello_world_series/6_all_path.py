from typing import List

# https://leetcode.com/problems/all-paths-from-source-to-target/submissions/


class Solution:

    # simple DFS program
    # we are not using the visited
    # bcz we want all the possible path
    # and for that if the visited then we will not be
    # able to make all the possible path
    # it will give unique path not all path

    def util(self, src, n, graph, ans, res, visited):

        if src == n - 1:
            ans.append(src)
            res.append(ans.copy())
            ans.pop()
            return

        visited[src] = True

        ans.append(src)

        for adj in graph[src]:
            # if not visited[adj]:
            self.util(adj, n, graph, ans, res, visited)

        ans.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [False] * (n + 1)
        ans = list()
        res = list()

        self.util(0, n, graph, ans, res, visited)

        return res
