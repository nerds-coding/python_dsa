# https://leetcode.com/problems/largest-divisible-subset/description/

from typing import List

# this problem is totally like the LIS
# one at the if we are taking he % mod and nothing else


class Solution:
    def largestDivisibleSubset(self, a: List[int]) -> List[int]:

        a.sort()
        n = len(a)
        dp = [1] * (n)
        tracking_list = [0] * n

        maxi = -1
        idx = 0
        for i in range(n):
            tracking_list[i] = i
            for j in range(i):
                if a[i] % a[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        tracking_list[i] = j

            if maxi < dp[i]:
                maxi = dp[i]
                idx = i

        ans = list()
        ans.append(a[idx])

        while tracking_list[idx] != idx:
            idx = tracking_list[idx]
            ans.append(a[idx])

        return ans
