# Find the last occurence of the element


def last_occurence(arr, x):
    low, res, high = 0, -1, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            res = mid + 1
            low = mid + 1  # b'coz we have to go more closer to the right side
            # right side is b'coz last occurence is possible there
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return res


print(last_occurence([1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5], 4))
