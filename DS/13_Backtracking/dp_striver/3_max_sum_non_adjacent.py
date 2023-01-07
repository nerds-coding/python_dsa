# https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1


class Solution:
    def max_sum(self, n, arr):

        if n == 0:
            return arr[n]

        if n < 0:
            return 0

        pick = self.max_sum(n - 2, arr) + arr[n]
        not_pick = self.max_sum(n - 1, arr) + 0

        return max(pick, not_pick)

    def findMaxSum(self, arr, n):
        return self.max_sum(n - 1, arr)
