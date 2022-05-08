"""
we have to count the occurence of element in sorted array.

eg : = [1,2,3,4,5,5,5,5,5,6,6,7,7,7,8,8,]

count of 5 = 4
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


def total_occurence_of_element(arr, x):
    """
    Reason for last - first occurence is

    suppose we found the
    first element at index 5
    and
    last element at index 7

    so the element is from 5 to 7
    which is = to 2 times occurence

    therefore 7-5 =2

    and
    +1
    b'coz we have 0 based index
    """
    return last_occurence(arr, x) - first_occurence(arr, x) + 1


print(
    total_occurence_of_element(
        [
            1,
            2,
            3,
            4,
            5,
            5,
            5,
            5,
            5,
            6,
            6,
            7,
            7,
            7,
            8,
            8,
        ],
        5,
    )
)
