# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1#

# https://astikanand.github.io/techblogs/dynamic-programming-patterns/unbounded-knapsack-pattern#introduction-
def knapSack(self, N, W, val, wt):

    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            not_consider = dp[i - 1][j]
            if j >= wt[i - 1]:

                rem_capacity = j - wt[i - 1]
                # * taking dp[i] bcz we can take the current
                # * item multiple times

                """
                i-1 --> mean taking what previous players have made
                
                i --> means taking our score and plus what we have 
                      achieved till that cell <max of (which can be our or previous player score)>
                
                """
                total_capacity = val[i - 1] + dp[i][rem_capacity]

                dp[i][j] = max(total_capacity, not_consider)
            else:
                dp[i][j] = not_consider

    return dp[N][W]
