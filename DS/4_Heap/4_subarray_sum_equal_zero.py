"""
Input: {4, 2, -3, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true

Explanation : 

The third element is zero. A single element is also a sub-array.

Input: {-3, 2, 3, 1, 6}
Output: false

"""


def subarray_sum_equal_zero(arr):
    prev_prefix = arr[0]

    total = set()

    for cur_sum in arr[1:]:
        if prev_prefix - cur_sum in total or cur_sum == 0:
            return True

        prev_prefix += cur_sum

        total.add(prev_prefix)

    return False


print(subarray_sum_equal_zero([4, 2, 0, 1, 6]))
