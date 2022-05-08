def maxProfit(prices):

    ans = 0

    temp = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < temp:

            print(temp)
        else:
            ans += prices[i] - temp
            temp = prices[i]
    return ans


print(maxProfit([1, 2, 3, 4, 5]))
