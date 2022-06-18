# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_element_in_sorted_array(arr, x):
    low, high = 0, len(arr) - 1
    n = len(arr)
    small = 0
    while low <= high:
        mid = low + (high - low) // 2

        prev = (mid + n - 1) % n
        next = (mid + 1) % n

        if arr[mid] < arr[prev] and arr[mid] < arr[next]:
            small = mid
            break
        elif arr[mid] < arr[high]:
            low = mid + 1
        else:
            high = mid - 1

    if binary_search(arr[small:], x) >= 0:
        return binary_search(arr[small:], x)
    else:
        return binary_search(arr[0:small], x)


arr = [6, 7, 8, 9, 1, 2, 3, 4, 5]
print(find_element_in_sorted_array(arr, 3))


# ---------------------- More optimized -----------------------------
# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/


# for explanation
# https://www.youtube.com/watch?v=oTfPJKGEHcc


def search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] >= arr[low]:
            if x >= arr[low] and arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if x <= arr[high] and arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [6, 6, 7, 8, 9, 1, 2, 3, 4, 5]
