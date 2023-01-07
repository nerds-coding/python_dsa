from typing import List


class Solution:

    dp = [[]]

    def util(self, i, j, arr):

        if i > j:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        maxi = -1e9

        for brust in range(i, j + 1):
            cur_ballon_cost = arr[i - 1] * arr[brust] * arr[j + 1]
            left = self.util(i, brust - 1, arr)
            right = self.util(brust + 1, j, arr)

            total_cost = cur_ballon_cost + left + right

            maxi = max(maxi, total_cost)

        self.dp[i][j] = maxi

        return self.dp[i][j]

    def maxCoins(self, N: int, arr: List[int]) -> int:

        arr.insert(0, 1)
        arr.append(1)

        dp = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

        for i in range(N, 0, -1):
            for j in range(1, N + 1):
                if i > j:
                    continue
                maxi = -1e9
                for brust in range(i, j + 1):
                    cur_ballon_cost = arr[i - 1] * arr[brust] * arr[j + 1]
                    left = dp[i][brust - 1]
                    right = dp[brust + 1][j]

                    total_cost = cur_ballon_cost + left + right

                    maxi = max(maxi, total_cost)

                dp[i][j] = maxi

        return dp[1][N]
