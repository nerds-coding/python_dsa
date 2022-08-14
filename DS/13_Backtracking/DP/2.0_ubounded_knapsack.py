# https://astikanand.github.io/techblogs/dynamic-programming-patterns/unbounded-knapsack-pattern


def unbounded_knapsack(capacity, item_profit, item_weight, item_len):

    if capacity == 0 or item_len == 0:
        return 0

    if capacity >= item_weight[item_len - 1]:

        """
        After taking the current item from the list
        we r againg calling the function with same item
        bcz repetition is allowed

        at some point after filling that item if we reach the same
        item cannot be filled again
        the we will enter into the else part

        and also in the starting
        we are taking both scenerio

        consider --> taking that item
        not_consider --> not taking that item

        (binary recursion at each call)

        """
        consider = item_profit[item_len - 1] + unbounded_knapsack(
            capacity - item_weight[item_len - 1], item_profit, item_weight, item_len
        )
        not_consider = unbounded_knapsack(capacity, item_profit, item_weight, item_len - 1)

        return max(consider, not_consider)
    else:
        not_consider = unbounded_knapsack(capacity, item_profit, item_weight, item_len - 1)

        return not_consider


print(unbounded_knapsack(8, [15, 50, 60, 90], [1, 3, 4, 5], 4))
