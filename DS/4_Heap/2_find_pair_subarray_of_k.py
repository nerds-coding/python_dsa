# https://www.techiedelight.com/find-subarrays-given-sum-array/

# this can also be used for
# given sum with 0
def find_pair_subarray_of_k(arr, k):
    ans = set()

    for i in arr:
        if k - i in ans:
            return True
        else:
            ans.add(i)

    return False


print(find_pair_subarray_of_k([1, 2, 3, 4, 5, 6, 9], 7))
