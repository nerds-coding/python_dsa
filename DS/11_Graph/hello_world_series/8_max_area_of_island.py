# https://leetcode.com/problems/max-area-of-island/

from typing import List


class Solution:

    # same logic as number of island
    # only keeping the record of area at reach side of the call

    # return function will be added to that direction from where it have
    # been called and then that direction
    # will return to it's recursive call function
    def dfs(self, r, c, row, col, grid, res):

        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != 1:
            return 0

        grid[r][c] = 2

        up = self.dfs(r + 1, c, row, col, grid, res)
        down = self.dfs(r - 1, c, row, col, grid, res)
        right = self.dfs(r, c + 1, row, col, grid, res)
        left = self.dfs(r, c - 1, row, col, grid, res)

        return 1 + up + down + right + left

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.ans = 0

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(i, j, row, col, grid, 0))

        return res
