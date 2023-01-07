# https://www.codingninjas.com/codestudio/problems/minimum-path-sum_985349?leftPanelTab=0


def minSumPath(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                down = grid[i][j]
                right = grid[i][j]

                if i > 0:
                    down += dp[i - 1][j]
                else:
                    down += 1e9

                if j > 0:
                    right += dp[i][j - 1]
                else:
                    right += 1e9

                dp[i][j] = min(down, right)

    return dp[row - 1][col - 1]
