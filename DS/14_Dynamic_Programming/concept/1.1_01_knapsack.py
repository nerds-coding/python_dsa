def knapsack(item_weight, profit, sack, item_len):

    # dp = [[0] * (sack + 1)] * (item_len + 1)

    dp = [[0 for x in range(sack + 1)] for y in range(item_len + 1)]
    for i in range(1, item_len + 1):
        for j in range(1, sack + 1):

            if j >= item_weight[i - 1]:

                team_capacity = (
                    j - item_weight[i - 1]
                )  # team_capacity if the player will play
                player_capacity = profit[i - 1]
                new_capacity = player_capacity + dp[i - 1][team_capacity]

                wont_play = dp[i - 1][j]

                dp[i][j] = max(wont_play, new_capacity)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp)
    print(dp[item_len][sack])


profit = [60, 100, 120]
items_weight = [10, 20, 30]
SACK = 50
n = len(profit)

knapsack(items_weight, profit, SACK, n)
