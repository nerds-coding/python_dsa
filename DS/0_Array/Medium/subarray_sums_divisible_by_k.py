# https://leetcode.com/problems/subarray-sums-divisible-by-k/

def subarraysDivByK(nums, k):
    subarray = [[]]
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(nums[i:j]%5==0)