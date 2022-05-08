# similar approach as 5th sum just also appended index with dictinary


def print_subarray_sum_equal_k(arr, k):
    prev_prefix = 0

    total = {}

    for i, cur in enumerate(arr):
        prev_prefix += cur

        if total.get(prev_prefix - k) or cur == k:
            return (total[prev_prefix - k], i + 1)

        total[prev_prefix] = i + 1

    return False


print(print_subarray_sum_equal_k([4, 1, 3, 7, 2, 5], 14))
