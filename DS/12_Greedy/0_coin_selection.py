# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/


def minimum_coin(coins, amount):

    number_of_coins = 0

    for i in coins:

        if i <= amount:
            max_coin_of_i = amount // i
            number_of_coins += max_coin_of_i

            amount -= max_coin_of_i * i

        if amount == 0:
            return number_of_coins


coins = [9, 6, 5, 1]

print(f"total number of coins required = {minimum_coin(coins, 11)}")
