import heapq


def spanningTree(V, adj):

    visited = [0] * V

    prev_distance = [float("inf")] * V
    parent = [-1] * V

    temp_list = list()

    heapq.heappush(temp_list, [0, 0])

    parent[0] = -1
    prev_distance[0] = 0

    while temp_list:

        cur_node_distance, cur_node = heapq.heappop(temp_list)

        visited[cur_node] = True

        for cur_adj_node, cur_adj_weight in adj[cur_node]:

            if (
                not visited[cur_adj_node]
                and cur_adj_weight < prev_distance[cur_adj_node]
            ):
                parent[cur_adj_node] = cur_node
                prev_distance[cur_adj_node] = cur_adj_weight

                heapq.heappush(temp_list, [cur_adj_weight, cur_adj_node])

    return sum(prev_distance)
