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

    def maxProfit(self, n: int, prices: List[int]) -> int:

        buy = 2
        capacity = 2
        dp = [
            [[0 for _ in range(capacity + 1)] for i in range(buy + 1)]
            for i in range(n + 1)
        ]

        for i in range(n - 1, -1, -1):
            # in buy we have 2 cases 0 -> don'nt buy
            #  1 buy it
            for buy in range(2):
                # starting from 1
                # bcz in recursive code if cap == 0
                # then we return the base case
                for cap in range(1, capacity + 1):
                    profit = 0
                    if buy:
                        buyit = -prices[i] + dp[i + 1][0][cap]
                        dont_buyit = 0 + dp[i + 1][1][cap]

                        profit = max(buyit, dont_buyit)
                    else:
                        sellit = prices[i] + dp[i + 1][1][cap - 1]
                        dont_sellit = 0 + dp[i + 1][0][cap]

                        profit = max(sellit, dont_sellit)

                    dp[i][buy][cap] = profit

        # returning the from the starting position of recursion
        #  were we passed the
        # 0 = idx
        # 1 = buy
        # 2 = capacity
        return dp[0][1][2]
