# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1#

"""
        Algorithm: 

    str1 and str2 be the given strings.
    m and n be their lengths respectively.
    len be the length of the longest common subsequence of str1 and str2
    minimum number of deletions minDel = m – len
    minimum number of Insertions minInsert = n – len
"""


def minOperations(self, s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return (len_s1 - dp[len_s1][len_s2]) + (len_s2 - dp[len_s1][len_s2])
