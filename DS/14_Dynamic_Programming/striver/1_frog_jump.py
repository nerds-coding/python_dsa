# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?leftPanelTab=0

# FIBONACCI Series
from typing import List


def frogJump(n: int, arr: List[int]) -> int:
    dp = [0] * n

    dp[0] = 0

    for i in range(1, n):
        first = dp[i - 1] + abs(arr[i] - arr[i - 1])

        second = float("inf")
        if i > 1:
            second = dp[i - 2] + abs(arr[i] - arr[i - 2])

        dp[i] = min(first, second)

    return dp[n - 1]


# without DP array
def frogJump(n: int, arr: List[int]) -> int:
    dp = [0] * n

    prev1 = 0
    prev2 = 0
    cur = 0
    for i in range(1, n):
        first = prev1 + abs(arr[i] - arr[i - 1])

        second = float("inf")
        if i > 1:
            second = prev2 + abs(arr[i] - arr[i - 2])

        cur = min(first, second)

        prev2 = prev1
        prev1 = cur

    return prev1
