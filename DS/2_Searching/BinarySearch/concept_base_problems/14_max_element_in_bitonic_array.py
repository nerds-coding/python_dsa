# https://www.callicoder.com/maximum-element-in-bitonic-array/


def max_element(arr):
    low, high, n = 0, len(arr) - 1, len(arr)

    while low <= high:
        mid = low + (high - low) // 2

        if (mid > 0) and (mid < n - 1):
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
        elif mid > 0 and arr[mid] > arr[mid - 1]:
            return arr[mid]
        elif mid < n - 1 and arr[mid] > arr[mid + 1]:
            return arr[mid]


print(max_element([2, 4, 6, 8, 10, 3, 1]))
