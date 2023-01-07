# https://leetcode.com/problems/minimum-falling-path-sum/description/


class Solution:
    def util(self, row, col, c, grid):

        if row < 0 or col < 0 or col >= c:
            return 1e9

        if row == 0:
            return grid[row][col]

        up = self.util(row - 1, col, c, grid) + grid[row][col]
        left_diag = self.util(row - 1, col - 1, c, grid) + grid[row][col]
        right_diag = self.util(row - 1, col + 1, c, grid) + grid[row][col]

        return min(up, left_diag, right_diag)

    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        ans = float("inf")

        for i in range(col - 1, -1, -1):
            ans = min(ans, self.util(row - 1, i, col, matrix))

        return ans
