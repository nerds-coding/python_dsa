def fourSum(nums, target):
    nums.sort()

    ans = []
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            new_target = target - (nums[i] + nums[j])
            l = j + 1
            k = n - 1
            tmp = list()
            while l < k:
                if nums[l] + nums[k] < new_target:
                    l += 1
                elif nums[l] + nums[k] > new_target:
                    k -= 1
                else:
                    tmp = [nums[i], nums[j], nums[l], nums[k]]

                    while l < k and nums[l] == tmp[2]:
                        l += 1
                    while l < k and nums[k] == tmp[3]:
                        k -= 1
                    ans.append(tmp)

            while (j < n - 3) and nums[j] == nums[j + 1]:
                j += 1
        while (nums[i] == nums[i + 1]) and (i < n - 3):
            i += 1

    return ans


print(fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
