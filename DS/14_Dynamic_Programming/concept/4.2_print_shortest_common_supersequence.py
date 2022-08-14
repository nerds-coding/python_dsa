# https://leetcode.com/problems/shortest-common-supersequence/

"""

Input: str1 = "abac", str2 = "cab"
Output: "cabac"

Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

"""


def print_shortestCommonSupersequence(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    dp = [[0 for _ in range(len_str1 + 1)] for _ in range(len_str2 + 1)]

    ans = ""
    for i in range(1, len_str2 + 1):
        for j in range(1, len_str1 + 1):

            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # printing the LCS
    # but also adding the biggest diagonal values
    # bcz now we are printing supersequence
    j, i = len_str1, len_str2
    while i > 0 and j > 0:
        if dp[i][j] > max(dp[i - 1][j], dp[i][j - 1]):
            ans += str2[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                ans += str2[i - 1]
                i -= 1
            else:
                ans += str1[j - 1]
                j -= 1

    while i > 0:
        ans += str2[i - 1]
        i -= 1
    while j > 0:
        ans += str1[j - 1]
        j -= 1
    return ans[::-1]


str1 = "abac"
str2 = "cab"

print(print_shortestCommonSupersequence(str1, str2))
