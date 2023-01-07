# https://practice.geeksforgeeks.org/problems/number-of-enclaves/1


# this problem is mixture of
# boundry dfs + max area of island


from typing import List


class Solution:

    # doing the boundry DFS traversals
    def dfs_boundry(self, r, c, row, col, grid):

        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != 1:
            return

        grid[r][c] = 3

        self.dfs_boundry(r + 1, c, row, col, grid)
        self.dfs_boundry(r - 1, c, row, col, grid)
        self.dfs_boundry(r, c + 1, row, col, grid)
        self.dfs_boundry(r, c - 1, row, col, grid)

    # max area of island
    def dfs_util(self, r, c, row, col, grid):
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != 1:
            return 0

        grid[r][c] = 3

        left = self.dfs_util(r + 1, c, row, col, grid)
        right = self.dfs_util(r - 1, c, row, col, grid)
        up = self.dfs_util(r, c + 1, row, col, grid)
        down = self.dfs_util(r, c - 1, row, col, grid)

        return 1 + left + right + up + down

    def numberOfEnclaves(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        # this part to check if all the grid is only of 1's
        count = True
        for i in range(row):
            if 0 in grid[i]:
                count = False
                break
        if count:
            return 0

        for i in range(row):
            if grid[i][0] == 1:
                self.dfs_boundry(i, 0, row, col, grid)
            if grid[i][col - 1] == 1:
                self.dfs_boundry(i, col - 1, row, col, grid)

        for j in range(col):
            if grid[0][j] == 1:
                self.dfs_boundry(0, j, row, col, grid)
            if grid[row - 1][j] == 1:
                self.dfs_boundry(row - 1, j, row, col, grid)

        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += self.dfs_util(i, j, row, col, grid)

        return ans
