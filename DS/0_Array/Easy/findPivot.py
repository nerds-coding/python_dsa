def pivotIndex(nums):

    n = len(nums)
    prefix = [0] * n
    sufix = [0] * n

    prefix[0] = nums[0]
    sufix[n - 1] = nums[n - 1]
    for i in range(1, n):
        prefix[i] = nums[i] + prefix[i - 1]
        sufix[n - i - 1] = nums[n - i - 1] + sufix[n - i]

    for i in range(0, n):
        if prefix[i] == sufix[i]:
            return i
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
