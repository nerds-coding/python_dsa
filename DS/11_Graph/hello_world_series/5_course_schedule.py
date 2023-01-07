# https://practice.geeksforgeeks.org/problems/course-schedule/1


# NEET CODE
# https://www.youtube.com/watch?v=Akt3glAwyfY


class Solution:
    def findOrder(self, n, m, prerequisites):

        graph = {adj: [] for adj in range(n)}

        for i in prerequisites:
            graph[i[0]].append(i[1])

        visited = set()
        cycle = set()

        ans = list()

        # this simple find cycle in Directed Graph
        # reason to check on src over adj
        # bcz some of the adj maybe dependent on other src node
        # so we are working on the src
        # which will be the final check that
        # no other adj is not dependent on it
        def dfs(src):

            # if we found cycle then return False
            # bcz no need to further check
            # bcz if we found any cycle
            # we cannot complete the whole course
            # thus return false
            if src in cycle:
                return False

            # if the src is visited
            # then return True bcz
            # we don't want to visit same src
            # and add duplicate value in ans
            if src in visited:
                return True

            cycle.add(src)
            for adj in graph[src]:
                # checking on NOT
                # bcz cycle is giving the False value
                if not dfs(adj):
                    return False

            # this typical directed graph cycle detection rule
            cycle.remove(src)
            visited.append(src)
            ans.append(src)
            return True

        for i in range(n):
            # if any point we found the cycle then it make no sense
            # to loop for the others
            if not dfs(i):
                return []

        return ans
