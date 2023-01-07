# https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1


class Solution:
    def island(self, r, c, row, col, grid):

        # if the current row and col of grid is not ==1
        # then it means it is already visited or there is blocker
        if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
            return

        grid[r][c] = 2

        self.island(r + 1, c, row, col, grid)
        self.island(r - 1, c, row, col, grid)
        self.island(r, c + 1, row, col, grid)
        self.island(r, c - 1, row, col, grid)
        self.island(r + 1, c + 1, row, col, grid)
        self.island(r - 1, c - 1, row, col, grid)
        self.island(r + 1, c - 1, row, col, grid)
        self.island(r - 1, c + 1, row, col, grid)

    def numIslands(self, grid):
        counter = 0

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.island(i, j, row, col, grid)
                    counter += 1

        return counter
