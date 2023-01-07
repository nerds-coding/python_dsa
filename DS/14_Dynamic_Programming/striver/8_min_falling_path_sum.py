
# https://leetcode.com/problems/minimum-falling-path-sum/description/


class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                
                if i == 0:
                    dp[i][j] = grid[i][j]
                else:

                    up = grid[i][j]
                    if i-1<0:
                        up+=1e9
                    else:
                        up += dp[i-1][j]

                    left_diag = grid[i][j]
                    if j-1<0:
                        left_diag+=1e9
                    else:
                        left_diag+= dp[i-1][j-1]

                    right_diag = grid[i][j]
                    if j+1>=col:
                        right_diag+=1e9
                    else: 
                        right_diag+= dp[i-1][j+1] 

                    dp[i][j] = min(up,left_diag,right_diag)
        # print(dp)
        return min(dp[row-1])




