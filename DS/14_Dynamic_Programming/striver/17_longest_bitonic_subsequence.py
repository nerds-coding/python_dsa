# https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1


    """
    Simple logic as LIS
    
    we are finding LIS ind Longest decreasing subsequence 
    both seperately
    
    and checking at which index both combination gives max val

    Returns:
        _type_: _description_
    """


class Solution:
    def LongestBitonicSequence(self, nums):
        n = len(nums)
        inc_dp = [1] * n
        dec_dp = [1] * n

        idx = 0
        tracking_list = [0] * n
        for i in range(n):
            tracking_list[i] = i
            for j in range(i):
                if nums[j] < nums[i]:
                    if inc_dp[j] + 1 > inc_dp[i]:
                        inc_dp[i] = 1 + inc_dp[j]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    dec_dp[i] = max(dec_dp[i], 1 + dec_dp[j])

        mx = 0
        for i in range(n):
            # -1 bcz one value will be common in both
            mx = max(mx, dec_dp[i] + inc_dp[i] - 1)
        return mx
