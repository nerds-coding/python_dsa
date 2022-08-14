def mcm(arr, i, j):

    if i >= j:
        return 0

    min_cal = float("inf")

    for k in range(i, j):  # (i,j) range will return from i to j-1
        temp_cal = mcm(arr, i, k) + mcm(arr, k + 1, j) + (arr[i - 1] * arr[k] * arr[j])

        min_cal = min(temp_cal, min_cal)

    return min_cal


arr = [1, 2, 3, 4, 3]
n = len(arr)

# if in the code we were calculating the j-1 then we can send n
# but we are calculating with the j thus we send n-1
print(mcm(arr, 1, n - 1))


# Python program using memoization
dp = [[-1 for i in range(100)] for j in range(100)]

# Function for matrix chain multiplication
def matrixChainMemoised(p, i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = float("inf")

    for k in range(i, j):
        dp[i][j] = min(
            dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        )

    return dp[i][j]


def MatrixChainOrder(p, n):
    i = 1
    j = n - 1
    return matrixChainMemoised(p, i, j)


# Driver Code
arr = [1, 2, 3, 4]
n = len(arr)
print("Minimum number of multiplications is", MatrixChainOrder(arr, n))

# This code is contributed by rag2127
