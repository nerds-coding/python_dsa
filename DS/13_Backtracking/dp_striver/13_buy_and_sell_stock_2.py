from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


class Solution:
    dp = [[]]

    # this problem is totally like
    # subset problem

    def util(self, price, buy, idx, n):

        # we reach beyond the index
        # we have to return 0
        # bcz even we have bought any stock
        # it don't matter now

        # abb bhai woh stock apne pass hi rakh
        if idx == n:
            return 0

        if self.dp[idx][buy] != -1:
            return self.dp[idx][buy]

        # if buy == 1
        # it means we are ready to buy new stock
        # we have permission from previous sales

        profit = 0
        if buy:
            # reason to -price[idx]
            # we have bought the stock
            # and somewhere in future we have sold that stock
            # then the recursive function will return the last stock price/profit

            # so from that we have to only calculate the profit
            buyit = -price[idx] + self.util(price, 0, idx + 1, n)
            dont_buyit = 0 + self.util(price, 1, idx + 1, n)

            profit = max(buyit, dont_buyit)
        else:
            # if buy == 0
            # then it means we have to sell the stock

            sellit = price[idx] + self.util(price, 1, idx + 1, n)
            dont_sellit = 0 + self.util(price, 0, idx + 1, n)

            profit = max(sellit, dont_sellit)

        self.dp[idx][buy] = profit

        return self.dp[idx][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # range only 2 
        # bcz we have only 2 option in columns
        # buyit or sell it
        self.dp = [[-1 for i in range(2)] for i in range(n + 1)]
        return self.util(prices, 1, 0, n)
