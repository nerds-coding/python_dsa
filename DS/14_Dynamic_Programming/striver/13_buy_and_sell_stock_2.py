class Solution:
    dp = [[]]

    def util(self, price, buy, idx, n):

        if idx == n:
            return 0

        if self.dp[idx][buy] != -1:
            return self.dp[idx][buy]

        # if buy == 0
        # then it means no we can't buy any new stock we have already bought it

        profit = 0
        if buy:
            buyit = -price[idx] + self.util(price, 0, idx + 1, n)
            dont_buyit = 0 + self.util(price, 1, idx + 1, n)

            profit = max(buyit, dont_buyit)
        else:
            sellit = price[idx] + self.util(price, 1, idx + 1, n)
            dont_sellit = 0 + self.util(price, 0, idx + 1, n)

            profit = max(sellit, dont_sellit)

        self.dp[idx][buy] = profit

        return self.dp[idx][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        

        dp = [[0 for i in range(2)] for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    buyit = -prices[i] + dp[i + 1][0]
                    dont_buyit = 0 + dp[i + 1][1]

                    profit = max(buyit, dont_buyit)
                else:
                    sellit = prices[i] + dp[i + 1][1]
                    dont_sellit = 0 + dp[i + 1][0]

                    profit = max(sellit, dont_sellit)

                dp[i][buy] = profit

        return dp[0][1]
