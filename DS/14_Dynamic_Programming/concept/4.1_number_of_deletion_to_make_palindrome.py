# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions4610/0/#

# same logic to make 4.0 only subtracting with len of string
# which means removing un-wanted chars from the string
def minDeletions(str1):
    str2 = str1[::-1]

    len_str1 = len(str1)
    len_str2 = len(str2)
    dp = [[0 for _ in range(len_str1 + 1)] for _ in range(len_str2 + 1)]

    for i in range(1, len_str2 + 1):
        for j in range(1, len_str1 + 1):

            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return len_str1 - dp[len_str2][len_str1]
