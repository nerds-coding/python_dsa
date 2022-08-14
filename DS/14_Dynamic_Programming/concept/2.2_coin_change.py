# https://practice.geeksforgeeks.org/problems/coin-change2448/1#


def count(S, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for j in range(1, n + 1):
        dp[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            not_consider = dp[i - 1][j]

            if j >= S[i - 1]:

                consider = dp[i][j - S[i - 1]]

                dp[i][j] = consider + not_consider
            else:
                dp[i][j] = not_consider

    return dp[m][n]


coins = [1, 2, 3]
n = len(coins)

change = 4

print(count(coins, n, change))
