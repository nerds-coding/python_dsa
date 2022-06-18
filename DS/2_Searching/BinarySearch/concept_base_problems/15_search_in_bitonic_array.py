# https://www.callicoder.com/search-in-bitonic-array/


def binary_search(arr, x, low, high):

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def search_in_bitonic_array(arr, x):
    low, high, n = 0, len(arr) - 1, len(arr)
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2

        if (mid > 0) and (mid < n - 1):
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                ans = mid
                break
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
        elif mid == 0 and arr[mid] > arr[mid - 1]:
            ans = mid
            break
        elif mid < n - 1 and arr[mid] > arr[mid + 1]:
            ans = mid
            break
    return max(binary_search(arr, x, 0, ans - 1), binary_search(arr[::-1], x, 0, ans))


print(search_in_bitonic_array([2, 4, 8, 10, 7, 6, 1], 6))
