# https://practice.geeksforgeeks.org/problems/number-of-unique-paths5339/1
class Solution:

    # Another Approach to solve the Prob
    # https://discuss.geeksforgeeks.org/comment/da98f22819dad36871b1af6b3de88be5
    def real_unique_path(self, row, col):

        # if we have one row then we have only one unique path
        # same for the col
        if row == 1 or col == 1:
            return 1

        return self.real_unique_path(row - 1, col) + self.real_unique_path(row, col - 1)

    def NumberOfPaths(self, a, b):
        # ---------------- DP Approach --------------
        # in reference of real_unique_path
        dp = [[1 for _ in range(b + 1)] for _ in range(a + 1)]

        for i in range(2, a + 1):
            for j in range(2, b + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[a][b]
