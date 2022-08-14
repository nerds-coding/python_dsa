class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        degree = [0] * V

        for i in range(V):
            for j in adj[i]:
                degree[j] += 1

        q = list()

        for val in range(V):
            if degree[val] == 0:
                q.append(val)

        ans = list()
        while q:
            cur = q.pop(0)

            ans.append(cur)

            for i in adj[cur]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)

        return ans
