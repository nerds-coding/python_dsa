""" 
we have to find the first occurence of element in given array

a = [1,1,1,2,2,2,2,2]
first occurence of 2 is at = 4 
"""


def first_occurence(arr, x):
    low, res, high = 0, -1, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            res = mid + 1
            high = mid - 1  # b'coz we have to go more closer to the left side
            # left side is b'coz first occurence is possible there
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return res


print(first_occurence([1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5], 4))
