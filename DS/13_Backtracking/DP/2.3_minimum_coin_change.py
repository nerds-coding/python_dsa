#https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/


    """
         this problem is mixture of 
         subset problem + rod change
    
    """


def min_coin(n, change, coins):

    if change == 0:
        return 0
    
    # using  "Infinity" bcoz if there is any change less than 0 or n==0
    # then the no such combination is possible
    # and also given in GFG practice to return infinity if no such combinatios
    if change < 0:
        return float("inf")

    if n == 0:
        return float("inf")

    if change >= coins[n - 1]:

        consider = 1 + min_coin(n, change - coins[n - 1], coins)

        not_consider = min_coin(n - 1, change, coins)

        return min(consider, not_consider)

    else:
        not_consider = min_coin(n - 1, change, coins)

        return not_consider


coins = [9, 6, 5, 1]
n = len(coins)
change = 11

print(min_coin(n, change, coins))
