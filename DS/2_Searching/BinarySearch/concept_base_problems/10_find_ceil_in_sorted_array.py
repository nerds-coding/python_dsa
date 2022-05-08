# https://www.techiedelight.com/find-floor-ceil-number-sorted-array/


def find_ceil_in_sorted_array(arr, x):
    low, high = 0, len(arr) - 1

    ceil = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1

    return ceil


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_ceil_in_sorted_array(arr, 10))
