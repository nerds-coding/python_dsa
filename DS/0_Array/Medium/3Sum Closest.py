# https://leetcode.com/problems/3sum-closest/


# https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            cur_res = nums[i] + nums[j] + nums[k]

            if cur_res == target:
                return cur_res

            if abs(cur_res - target) < abs(res - target):
                res = cur_res

            if cur_res < target:
                j += 1
            else:
                k -= 1
    return res


print(threeSumClosest(nums=[0, 0, 0], target=1))
