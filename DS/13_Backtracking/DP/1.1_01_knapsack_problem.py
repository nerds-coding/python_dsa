# https://www.interviewbit.com/blog/0-1-knapsack-problem/


def knapsack(items_weight, profit, sack, item_len, ans):

    if sack == 0 or item_len == 0:
        return ans

    if items_weight[item_len] <= sack:
        consider = knapsack(
            items_weight,
            profit,
            sack - items_weight[item_len],
            item_len - 1,
            ans + profit[item_len],
        )

        not_consider = knapsack(items_weight, profit, sack, item_len - 1, ans)
        return max(consider, not_consider)
    else:
        return knapsack(items_weight, profit, sack, item_len, ans)


profit = [60, 100, 120]
items_weight = [10, 20, 30]
SACK = 50
n = len(profit) - 1
print(knapsack(items_weight, profit, SACK, n, 0))


def knapsack(item_weight, profit, sack, item_len):

    if sack == 0 or item_len == 0:
        return 0

    if sack >= item_weight[item_len]:
        return max(
            profit[item_len]
            + knapsack(item_weight, profit, sack - item_weight[item_len], item_len - 1),
            knapsack(item_weight, profit, sack, item_len - 1),
        )
    else:
        return knapsack(item_weight, profit, sack, item_len - 1)


print(knapsack(items_weight, profit, SACK, n))
