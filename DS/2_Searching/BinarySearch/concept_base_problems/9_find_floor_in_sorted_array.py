# https://www.techiedelight.com/find-floor-ceil-number-sorted-array/


def find_floor_in_sorted_array(arr, x):
    low, high = 0, len(arr) - 1

    floor = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1

    return floor


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_floor_in_sorted_array(arr, 1))
