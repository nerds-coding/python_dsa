from typing import List


"""  
    part 4 is totally same only space optimization is done in the video of striver
    
    part 5 is not but one day of cooldown (means after selling, just next day we can't buy the shares
    we have to take atleast one day of rest
    )
    so while selling the stock we will do the 
    idx+2
"""

class Solution:

    dp = [[[]]]

    def util(self, price, n, idx, buy, capacity):

        if self.dp[idx][buy][capacity] != -1:
            return self.dp[idx][buy][capacity]

        if idx == n or capacity == 0:
            return 0

        profit = 0

        if buy:
            buy_it = -price[idx] + self.util(price, n, idx + 1, 0, capacity)
            dont_buy_it = 0 + self.util(price, n, idx + 1, 1, capacity)

            profit = max(buy_it, dont_buy_it)
        else:
            # here we are making one complete cycle of
            # BUY and SELL
            sell_it = price[idx] + self.util(price, n, idx + 1, 1, capacity - 1)

            # here we are again keeping that stock for future analysis
            dont_sell_it = 0 + self.util(price, n, idx + 1, 0, capacity)

            profit = max(sell_it, dont_sell_it)

        self.dp[idx][buy][capacity] = profit
        return self.dp[idx][buy][capacity]

    def maxProfit(self, n: int, price: List[int]) -> int:
        capacity = 2
        self.dp = [
            [[-1 for _ in range(capacity + 1)] for i in range(2 + 1)]
            for i in range(n + 1)
        ]
        # capacity can change and this code work for all the possible capacity
        return self.util(price, n, 0, 1, capacity)
