# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
# https://www.techiedelight.com/find-peak-element-array/


def peak_element(arr):
    low, high, n = 0, len(arr) - 1, len(arr)

    while low <= high:

        mid = low + (high - low) // 2

        if mid > 0 and mid < n:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        elif mid == 0 and arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif mid == n - 1 and arr[mid] > arr[mid - 1]:
            return arr[mid]
    return -1


print(peak_element([10, 20, 15, 2, 23, 90, 67]))
