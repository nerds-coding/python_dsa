def minimum_subset_sum_difference(arr, n, total, new_subset):
    
    """
    minimum = abs(sum_of_subset_1 - sum_of_subset_2)
    minimum - sum_of_subset_1 = sum_of_subset_2
    """
    
    if n == 0:
        return abs(abs(total - new_subset) - new_subset)

    consider = minimum_subset_sum_difference(arr, n - 1, total, new_subset + arr[n - 1])
    not_consider = minimum_subset_sum_difference(arr, n - 1, total, new_subset)

    return min(consider, not_consider)


arr = [1, 6, 11, 5]
total = sum(arr)
n = len(arr)

print(minimum_subset_sum_difference(arr, n, total, 0))
