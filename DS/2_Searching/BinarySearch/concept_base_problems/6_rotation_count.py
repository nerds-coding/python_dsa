# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/


def rotation_count(arr):
    low, high = 0, len(arr) - 1
    n = len(arr)

    while low <= high:
        mid = low + (high - low) // 2

        prev = (mid + n - 1) % n
        next = (mid + 1) % n

        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            return mid
        elif arr[mid] < arr[high]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [6, 7, 0, 1, 2, 3, 4, 5]
print(rotation_count(arr))
