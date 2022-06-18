# https://leetcode.com/problems/find-the-duplicate-number/

def remove_duplicates(nums):
    for i in range(0, len(nums)):
        nums[i] = -nums[i]

    for i in range(0, len(nums)):
        if(nums[abs(nums[i])-1] < 0):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1])
        else:
            return abs(nums[i])


print(remove_duplicates([1, 3, 4, 2, 2]))
