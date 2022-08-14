def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [-2, 45, 0, 11, -9]
print(selection_sort(arr))
