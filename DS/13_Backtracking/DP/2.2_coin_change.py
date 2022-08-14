def coin_change(coins, change, n):

    if change == 0:
        return 1

    if n == 0:
        return 0

    if change >= coins[n - 1]:
        consider = coin_change(coins, change - coins[n - 1], n)

        not_consider = coin_change(coins, change, n - 1)

        return consider + not_consider
    else:
        not_consider = coin_change(coins, change, n - 1)
        return not_consider


coins = [1, 2, 3]
n = len(coins)

change = 4
print(coin_change(coins, change, n))
