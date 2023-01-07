# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # https://leetcode.com/problems/unique-paths-ii/solutions/1180249/easy-solutions-w-explanation-comments-optimization-from-brute-force-approach/?orderBy=most_votes
        # if obstacleGrid[0][0] == 1:
        #     return 0

        # row = len(obstacleGrid)
        # col = len(obstacleGrid[0])
        # # return self.unique_path(row-1,col-1,row,col,obstacleGrid)

        # dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        # dp[0][1] = 1

        # for i in range(1,row+1):
        #     for j in range(1,col+1):
        #         if obstacleGrid[i-1][j-1]==0:
        #             dp[i][j] = dp[i-1][j]+dp[i][j-1]

        # return dp[row][col]

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = 0
                    down = 0

                    if i > 0:
                        up = dp[i - 1][j]

                    if j > 0:
                        down = dp[i][j - 1]
                    dp[i][j] = up + down

        return dp[row - 1][col - 1]
