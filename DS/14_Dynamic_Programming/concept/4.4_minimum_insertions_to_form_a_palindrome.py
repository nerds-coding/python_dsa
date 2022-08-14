# https://practice.geeksforgeeks.org/problems/form-a-palindrome1455/1


# similar logic as number of deletion to make a string palindrome

# to make string palindrome we have certain amount of chars
# so instead of deleting the char we should add that same chars in original string


def countMin(self, str1):
    n = len(str1)
    str2 = str1[::-1]
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return n - dp[n][n]
