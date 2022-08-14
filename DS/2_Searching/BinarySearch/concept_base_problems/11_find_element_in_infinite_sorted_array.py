def find_element_in_infinite_sorted_array(arr, x):
    low = 0
    high = x

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            high = high + x
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(
    find_element_in_infinite_sorted_array(
        [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 9, 9, 9, 9, 9, 9, 10], 5
    )
)


# Another Approach


def find_element(arr, x):
    low, high = 0, 1

    while arr[high] < x:
        low = high
        high *= 2

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(
    find_element(
        [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 9, 9, 9, 9, 9, 9, 10], 5
    )
)
