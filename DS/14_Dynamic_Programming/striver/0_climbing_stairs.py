# https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1

# Totaly similar to Fibonacci


class Solution:
    # Function to count number of ways to reach the nth stair.
    def countWays(self, n):

        # if n == 0:
        #     return 1

        # if n<0:
        #     return 0

        # return self.countWays(n-1)+self.countWays(n-2)

        dp = [0] * (n + 1)
        mod = 10**9 + 7
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):

            if i - 1 < 0:
                prev1 = 0
            else:
                prev1 = dp[i - 1]

            if i - 2 < 0:
                prev2 = 0
            else:
                prev2 = dp[i - 2]

            dp[i] = (prev2 + prev1) % mod

        return dp[n]
