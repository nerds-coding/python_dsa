# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)


sol = Solution()
print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
