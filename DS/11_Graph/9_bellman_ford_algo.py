class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    """
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    """

    def bellman_ford(self, V, adj, S):

        distance = [100000000] * V

        distance[S] = 0

        for i in range(V - 1):
            for src, dest, dist in adj:
                # Because adding something to INT_MAX generates an overflow which makes the value negative leading
                if (
                    distance[src] != float("inf")
                    and distance[dest] > distance[src] + dist
                ):
                    distance[dest] = distance[src] + dist

        # for negative cycle
        for src, dest, dist in adj:
            if distance[src] != float("inf") and distance[dest] > distance[src] + dist:
                return
        return distance
