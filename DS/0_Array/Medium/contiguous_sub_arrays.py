def subarray(arr):
    n = len(arr)

    for i in range(n):
        for j in range(1, n - i + 1):
            print(arr[i : i + j])


subarray([1, 2, 3, 4])
