def fractional_knapsack(sack, capacity):
    max_profit = 0

    sack = sorted(sack, key=lambda x: x[0] / x[1], reverse=True)

    print(sack)
    for i in sack:
        if i[1] <= capacity:
            capacity -= i[1]
            max_profit += i[0]
        else:
            max_profit += i[0] * (capacity / i[1])
            return max_profit


sack = [[60, 10], [100, 20], [120, 30]]
print(fractional_knapsack(sack, 50))
