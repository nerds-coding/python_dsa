def k_jump_frog(n, arr, ans, k):

    if n == 0:
        return 0

    
    for i in range(1, k + 1):
        m = float("inf")
        if n - i >= 0:
            m = k_jump_frog(n - i, arr, ans, k) + abs(arr[n] - arr[n - i])
        ans[0] = min(ans[0], m)

    
    return m


arr = [30, 10, 60, 10, 60, 50]
n = len(arr) - 1
k = 2
ans = [float("inf")]
k_jump_frog(n, arr, ans, k)

print(ans)
