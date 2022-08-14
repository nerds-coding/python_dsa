# https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1#


def lcs(str1, str2, str1_len, str2_len):

    dp = [[0 for _ in range(str1_len + 1)] for _ in range(str2_len + 1)]

    for i in range(1, str2_len + 1):
        for j in range(1, str1_len + 1):

            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[str2_len][str1_len]


str1 = "abcdefgh"
str2 = "abcegh"

print(lcs(str1, str2, len(str1), len(str2)))
