# https://www.interviewbit.com/blog/subarray-sum-equals-k/


def subarray_sum_equal_k(arr, k):

    prev_prefix = 0
    total = set()

    for cur in arr:
        prev_prefix += cur
        if prev_prefix - k in total or cur == 0:
            print(prev_prefix)
            return True
        total.add(prev_prefix)

    return False

print(subarray_sum_equal_k([4, 1, 3, 7, 2, 5], 14))
