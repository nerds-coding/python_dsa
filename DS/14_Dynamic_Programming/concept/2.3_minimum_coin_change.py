# https://practice.geeksforgeeks.org/problems/number-of-coins1824/1#

"""
         this problem is mixture of 
         subset problem + rod change
    
"""


def minCoins(coins, M, V):

    dp = [[0 for _ in range(V + 1)] for _ in range(M + 1)]

    # using  "Infinity" bcoz if there is any change less than 0 or n==0
    # then the no such combination is possible
    # and also given in GFG practice to return infinity if no such combinatios
    for j in range(1, V + 1):
        dp[0][j] = float("inf")

    for i in range(1, M + 1):
        for j in range(1, V + 1):

            not_consider = dp[i - 1][j]

            if j >= coins[i - 1]:

                consider = 1 + dp[i][j - coins[i - 1]]

                dp[i][j] = min(consider, not_consider)

            else:
                dp[i][j] = not_consider

    return dp[M][V] if dp[M][V] != float("inf") else -1


coins = [9, 6, 5, 1]
n = len(coins)
change = 11

print(minCoins(coins, n, change))
