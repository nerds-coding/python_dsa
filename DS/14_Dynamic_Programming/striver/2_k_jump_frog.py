# https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-distances-dp-4/


def k_jump_frog(n, arr, k):
    dp = [0] * n
    ans = float("inf")
    for i in range(1, n):
        m = float("inf")
        for jump in range(1, k + 1):
            if i - jump >= 0:
                m = dp[i - jump] + abs(arr[i] - arr[i - jump])
                ans = min(ans, m)
        dp[i] = ans

    return dp[n - 1]


arr = [30, 10, 60, 10, 60, 50]
n = len(arr) - 1
k = 2
ans = [float("inf")]
print(k_jump_frog(n, arr, k))
