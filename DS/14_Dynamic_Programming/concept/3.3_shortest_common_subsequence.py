# https://practice.geeksforgeeks.org/problems/shortest-common-supersequence0322/1#

"""
    X = abcd, Y = xycd
    Output: 6
    Explanation: Shortest Common Supersequence
    would be abxycd which is of length 6 and
    has both the strings as its subsequences.
    
    as we can see that there is few char are commno among them
    (which we can call them lcs)
    
    so abcdxycd-(1 time common words then) = shortest common subsequence
    
    
    Length of the shortest supersequence  = 
    (Sum of lengths of given two strings) - (Length of LCS of two given strings) 

"""


def shortestCommonSupersequence(self, X, Y, m, n):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if Y[i - 1] == X[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return (m + n) - dp[n][m]
