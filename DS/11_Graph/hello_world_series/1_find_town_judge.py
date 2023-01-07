# https://leetcode.com/problems/find-the-town-judge/submissions/


def findJudge(self, n: int, trust: List[List[int]]) -> int:

    # bcz this problem is easy thus no need of outdegree
    # we will be using only indegree

    if n == 1 and trust == []:
        return 1

    indg = [0] * (n + 1)

    for cur in trust:
        indg[cur[0]] -= 1
        indg[cur[1]] += 1

    for i in range(n + 1):
        if indg[i] == n - 1:
            return i

    return -1
