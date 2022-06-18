def simple_bubble_sort(arr):
    n = len(arr)

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def optimized_bubble_sort(arr):
    n = len(arr)

    for i in range(0, n):
        swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            return arr


arr = [2, 4, 6, 8, 9, 1, 3, 5, 7]
print(simple_bubble_sort(arr))

print(optimized_bubble_sort(arr))
