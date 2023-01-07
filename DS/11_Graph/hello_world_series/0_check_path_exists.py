# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/


def validPath(
    self, n: int, edges: List[List[int]], source: int, destination: int
) -> bool:

    # the graph in given in source and destination pair
    # so we will convert into vertex list representation to BFS

    if source == destination:
        return True

    graph = dict()

    visited = [False] * (n + 1)

    q = [source]
    visited[source] = True

    # now making the graph
    for cur in edges:
        graph[cur[0]] = [cur[1]] + graph.get(cur[0], [])
        graph[cur[1]] = [cur[0]] + graph.get(cur[1], [])

    # now doing the BFS
    while q:
        cur = q.pop(0)

        for adj in graph[cur]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True
            if visited[destination]:
                return True
