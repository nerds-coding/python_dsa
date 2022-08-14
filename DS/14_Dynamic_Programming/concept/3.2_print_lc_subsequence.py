# this simple brute force technique with DP


def print_lc_subsequence(str1, str2, str1_len, str2_len):

    dp = [[0 for _ in range(str2_len + 1)] for _ in range(str1_len + 1)]

    ans = set()
    k = 0
    for i in range(1, str1_len + 1):
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                ans.add((k, str1[i - 1]))
                k += 1
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return sorted(ans, key=lambda x: x[0])


str1 = "abcdef"
str2 = "abceg"

str1_len = len(str1)
str2_len = len(str2)

print(print_lc_subsequence(str1, str2, str1_len, str2_len))
