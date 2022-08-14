def bs_in_descending(arr, x):

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid + 1

        elif arr[mid] > x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(bs_in_descending([9, 8, 7, 6, 5, 4, 3, 2, 1], 1))
