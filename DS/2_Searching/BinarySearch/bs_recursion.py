def binary_search_recursion(arr, x, low, high):
    mid = (low + high) // 2
    if low <= high:
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            high = mid - 1
            return binary_search_recursion(arr, x, low, high)
        else:
            low = mid + 1
            return binary_search_recursion(arr, x, low, high)

    else:
        return "No such element"


print(binary_search_recursion([1, 2, 3, 4, 5, 6, 7, 8], 1, 0, 8))


"""
Binary Search Complexity


Time Complexities
Best case complexity: O(1)
Average case complexity: O(log n)
Worst case complexity: O(log n)


Space Complexity
The space complexity of the binary search is O(1)

"""
