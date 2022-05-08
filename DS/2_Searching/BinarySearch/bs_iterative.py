def binary_search_iterative(arr, x):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return "No such element"


print(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8], 1))

"""
Binary Search Complexity


Time Complexities
Best case complexity: O(1)
Average case complexity: O(log n)
Worst case complexity: O(log n)


Space Complexity
The space complexity of the binary search is O(1)

"""
