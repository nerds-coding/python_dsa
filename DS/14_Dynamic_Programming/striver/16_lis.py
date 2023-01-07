# User function Template for python3


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
        # one bcz every element is LIS of itself
        dp = [1] * (n)

        for i in range(n):
            for j in range(i):
                if a[i] > a[j]:
                    dp[i] = max(1 + dp[j], dp[i])

        return max(dp)


# ----------- PRINTING THE SUBSEQUENCES ---------------


def print_longestSubsequence(a, n):
    # one bcz every element is LIS of itself
    dp = [1] * (n)
    tracking_list = [i for i in range(n)]
    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                if 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    tracking_list[i] = j

    max_idx = -1
    val = -1
    for i in range(len(dp)):
        if val < dp[i]:
            val = dp[i]
            max_idx = i

    while tracking_list[max_idx] != max_idx:
        ans.append(a[max_idx])

        max_idx = tracking_list[max_idx]

    ans.append(a[max_idx])

    return ans[::-1]


# ------------ LIS Using Binary Search ------------

    """
    
    STRIVER BHAIY KI JAI HO
        
    """


def longestSubsequence(a, n):
    from bisect import bisect_left

    ans = list()
    ans.append(a[0])
    for i in range(1, n):
        if ans and ans[-1] < a[i]:
            ans.append(a[i])
        else:
            lower = bisect_left(ans, a[i])
            ans[lower] = a[i]

    return len(ans)
