# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/#:~:text=So%20the%20Rod%20Cutting%20problem,in%20a%20bottom%2Dup%20manner.

"""
    It is similar like the Unbounded knapsack problem
    without any changes
    
    it is unbounded knapsack 2.0
    
    
    if the lenghts of rod is not given 
    it means we have lenght of rod from 1 to rod_len 

"""

def rod_cutting(rod_len, profit_len, profit, lengths):

    if not rod_len or not profit_len:
        return 0

    if rod_len >= lengths[profit_len - 1]:

        consider_repetition = rod_cutting(rod_len - lengths[profit_len - 1], profit_len - 1, profit, lengths)

        add_profit = profit[profit_len - 1] + consider_repetition

        not_consider = rod_cutting(rod_len, profit_len - 1, profit, lengths)

        return max(add_profit, not_consider)
    else:
        return rod_cutting(rod_len, profit_len - 1, profit, lengths)


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)

lengths = [i for i in range(1, size + 1)]

print(rod_cutting(size, size, arr, lengths))
