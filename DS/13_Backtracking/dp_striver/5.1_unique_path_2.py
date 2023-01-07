# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List


class Solution:
    def unique_path(self, row, col, r, c, grid):

        if row < 0 or row >= r or col < 0 or col >= c or grid[row][col] == 1:
            return 0

        if row == 0 and col == 0:
            return 1

        return self.unique_path(row - 1, col, r, c, grid) + self.unique_path(
            row, col - 1, r, c, grid
        )

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # https://leetcode.com/problems/unique-paths-ii/solutions/1180249/easy-solutions-w-explanation-comments-optimization-from-brute-force-approach/?orderBy=most_votes
        if obstacleGrid[0][0] == 1:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        return self.unique_path(row - 1, col - 1, row, col, obstacleGrid)
