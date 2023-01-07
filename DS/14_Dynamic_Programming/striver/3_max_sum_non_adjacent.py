# https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1
def findMaxSum(arr, n):
    if n == 0:
        return arr[0]

    dp = [0] * n
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        pick = dp[i - 2] + arr[i]
        not_pick = dp[i - 1] + 0

        dp[i] = max(pick, not_pick)
    return dp[n - 1]
