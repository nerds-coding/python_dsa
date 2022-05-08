# https://www.callicoder.com/minimum-difference-element-in-sorted-array/

def minimum_difference(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return x
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return min(abs(arr[low] - x), abs(arr[high] - x))


print(minimum_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14], 10))
