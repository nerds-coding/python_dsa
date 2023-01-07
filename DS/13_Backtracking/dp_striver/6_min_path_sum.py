# https://www.codingninjas.com/codestudio/problems/minimum-path-sum_985349?leftPanelTab=0

def util(row, col, grid):

    if row < 0 or col < 0:
        return float("inf")

    if row == 0 and col == 0:
        return grid[row][col]

    down = util(row - 1, col, grid)
    right = util(row, col - 1, grid)

    return grid[row][col] + min(down, right)


def minSumPath(grid):
    row = len(grid)
    col = len(grid[0])
    return util(row - 1, col - 1, grid)
