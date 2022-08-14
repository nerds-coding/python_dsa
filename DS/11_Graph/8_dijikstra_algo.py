import heapq


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):

        parent = [-1] * V

        prev_weight = [float("inf")] * V

        temp_list = list()

        heapq.heappush(temp_list, [0, S])

        prev_weight[S] = 0

        visited = [False] * V
        while temp_list:

            cur_weight, cur_node = heapq.heappop(temp_list)

            # visited[cur_node] = True

            for cur_adj_node, cur_adj_node_weight in adj[cur_node]:

                if prev_weight[cur_adj_node] > cur_adj_node_weight + cur_weight:

                    parent[cur_adj_node] = cur_node

                    prev_weight[cur_adj_node] = cur_adj_node_weight + cur_weight

                    heapq.heappush(temp_list, [prev_weight[cur_adj_node], cur_adj_node])

        return prev_weight
