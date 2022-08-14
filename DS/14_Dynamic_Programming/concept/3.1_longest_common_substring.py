# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1#


def longestCommonSubstr(self, str1, str2, str1_len, str2_len):

    dp = [[0 for _ in range(str1_len + 1)] for _ in range(str2_len + 1)]

    max_str = 0

    for i in range(1, str2_len + 1):
        for j in range(1, str1_len + 1):

            if str2[i - 1] == str1[j - 1]:
                prev_max_subtring = dp[i - 1][j - 1]
                dp[i][j] = 1 + prev_max_subtring

                # using max_str bcoz "LCS" can be in-middle of matrix also
                max_str = max(max_str, dp[i][j])
            else:
                # 0 bcoz we want contionus
                dp[i][j] = 0

        return max_str
