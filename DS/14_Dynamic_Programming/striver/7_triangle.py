# https://leetcode.com/problems/triangle/solutions/2146264/c-python-simple-solution-w-explanation-recursion-dp/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        col = len(triangle[0])

        dp = [[0 for i in range(row)] for _ in range(row)]

        dp[row - 1] = triangle[row - 1]
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                down = triangle[i][j] + dp[i + 1][j]
                right = triangle[i][j] + dp[i + 1][j + 1]

                dp[i][j] = min(right, down)

            # print(dp)
        return dp[0][0]

        # --------- 1D DP ----------
        row = len(triangle)
        col = len(triangle[0])

        dp = [0] * row

        dp = triangle[row - 1]
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                down = triangle[i][j] + dp[j]
                right = triangle[i][j] + dp[j + 1]

                dp[j] = min(right, down)

            # print(dp)
        return dp[0]
