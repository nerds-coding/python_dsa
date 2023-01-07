# https://leetcode.com/problems/number-of-longest-increasing-subsequence/submissions/

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        # this for keep the record number of subsequence of that specific lenght
        count = [1] * n

        maxi = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lis[i] < 1 + lis[j]:
                        lis[i] = 1 + lis[j]

                        # in this if condition
                        # we are getting new lenght of susbequence
                        # thus we are just copying the length of old
                        # possible subsequence
                        count[i] = count[j]
                    elif lis[i] == 1 + lis[j]:
                        # in this conditoin we have already same length of susbsequence
                        # but we get one more
                        # thus we are keeping till  that how much it is possible
                        count[i] += count[j]

            if lis[i] > maxi:
                maxi = lis[i]

        ans = 0
        for i in range(n):
            if lis[i] == maxi:
                ans += count[i]

        return ans
