# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1#


def cutRod(price, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            not_consider = dp[i - 1][j]

            if j >= i:
                consider = price[i - 1] + dp[i][j - i]

                dp[i][j] = max(consider, not_consider)
            else:
                dp[i][j] = not_consider

    return dp[n][n]


# profit associated with each length
arr = [1, 5, 8, 9, 10, 17, 17, 20]

# length of the rod
size = len(arr)

print(cutRod(arr, size))
