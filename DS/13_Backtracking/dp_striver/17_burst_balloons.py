from typing import List

# https://practice.geeksforgeeks.org/problems/burst-balloons/1


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

        self.dp = [[-1 for _ in range(N + 1)] for i in range(N + 1)]
        arr.insert(0, 1)
        arr.append(1)

        return self.util(1, N, arr)
