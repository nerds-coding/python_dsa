def removeDuplicates(nums):
    # same logic as move all zeros to last
    # but instead of original we take account of original +1
    original = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[original]:
            nums[i], nums[original + 1] = nums[original + 1], nums[i]
            original += 1
    return original + 1


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(arr[: removeDuplicates(arr)])
