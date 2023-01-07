# https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1


class Solution:

    dp = dict()

    def util(self, arr, idx, n, prev):

        if (idx, prev) in self.dp:
            return self.dp[(idx, prev)]

        if idx == 0:
            return 0

        if prev == -1 or prev > arr[idx - 1]:
            take_it = self.util(arr, idx - 1, n, arr[idx - 1]) + 1
            dont_take_it = self.util(arr, idx - 1, n, prev)

            self.dp[(idx, prev)] = max(take_it, dont_take_it)
            return self.dp[(idx, prev)]
        else:
            self.dp[(idx, prev)] = self.util(arr, idx - 1, n, prev)
            return self.dp[(idx, prev)]

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        return self.util(a, n, n, float("inf"))
