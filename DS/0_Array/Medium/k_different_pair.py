# https://leetcode.com/problems/k-diff-pairs-in-an-array/


def binary_search(nums, n, new_k):
    i = 0
    j = n - 1
    while (i <= j):
        mid = (i + j) // 2
        if (nums[mid] < new_k):
            i = mid + 1
        elif (nums[mid] > new_k):
            j = mid - 1
        else:
            return nums[mid]


def findPairs(nums, k):
    n = len(nums)
    nums.sort()
    ans = set()

    for x in nums:
        temp = binary_search(nums, n, k + x)
        if (temp):
            ans.add((x, temp))

    return ans


print(findPairs(nums=[3, 1, 4, 1, 5], k=2))
