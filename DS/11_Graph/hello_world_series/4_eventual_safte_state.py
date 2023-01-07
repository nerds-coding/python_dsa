# https://practice.geeksforgeeks.org/problems/eventual-safe-states/1

from typing import List


"""
        The logic is very simple 
        we just have to find out the cycle is present or not
        
        reason to find out cycle is present or not 
        is bcz if there is cycle then that node may fall into that cycle
        and never reach to the terminal node
        SO mereko thoda bhi risk nhi lene ka hai re baba
        
        so we only add those node which are not into cycle or itself the termianl node
        
        nodes which are not in the cycle will eventually any how reach to terminal node
        or they will be the termianl node
"""


class Solution:
    def is_cycle(self, src, graph, visited, path, terminal):

        visited[src] = True
        path[src] = True

        for adj in graph[src]:
            if not visited[adj]:
                if self.is_cycle(adj, graph, visited, path, terminal):
                    return True
            elif path[adj]:
                return True

        path[src] = False
        return False

    def eventualSafeNodes(self, V: int, graph: List[List[int]]) -> List[int]:

        visited = [False] * V
        path = [False] * V
        terminal = [False] * V

        for i in range(V):
            if not self.is_cycle(i, adj, visited, path, terminal):
                terminal[i] = True

        ans = set()
        for i in range(len(terminal)):
            if not terminal[i]:
                ans.add(i)

        return list(ans)
