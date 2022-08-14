# https://www.geeksforgeeks.org/search-almost-sorted-array/


def search_in_nearly_sorted_array(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif mid - 1 >= low and arr[mid - 1] == x:
            return mid - 1
        elif mid + 1 <= high and arr[mid + 1] == x:
            return mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(search_in_nearly_sorted_array([10, 3, 40, 20, 50, 80, 70], 40))
