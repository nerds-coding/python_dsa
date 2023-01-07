# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

# MCM


class Solution:

    dp = [[]]

    def util(self, i, j, cuts):

        if i > j:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]
        mini = 1e9

        for cut in range(i, j + 1):
            left_cost = self.util(i, cut - 1, cuts)
            right_cost = self.util(cut + 1, j, cuts)

            total_len_cost = cuts[j + 1] - cuts[i - 1]

            ans = total_len_cost + left_cost + right_cost

            mini = min(mini, ans)

        self.dp[i][j] = mini
        return self.dp[i][j]

    def minCost(self, n: int, cuts: List[int]) -> int:

        c = len(cuts)

        self.dp = [[-1 for _ in range(n + 1)] for j in range(c + 1)]

        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()

        return self.util(1, c, cuts)
