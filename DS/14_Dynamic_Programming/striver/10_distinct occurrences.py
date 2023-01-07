# Yhttps://practice.geeksforgeeks.org/problems/distinct-occurrences/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
class Solution:
    def sequenceCount(self, arr1, arr2):
        mod = (10**9) + 7
        n = len(arr1)
        m = len(arr2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                not_consider = dp[i - 1][j]
                if arr1[i - 1] == arr2[j - 1]:
                    consider = dp[i - 1][j - 1]

                    dp[i][j] = (consider + not_consider) % mod
                else:
                    dp[i][j] = (not_consider) % mod

        return dp[n][m]
