# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

def minimum_subset_sum_difference(arr,n):
    total= sum(arr)
    
    dp = [[0 for _ in range(total+1)] for i in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for j in range(1,total+1):
        dp[0][j] = False
    
    
    for i in range(1,n+1):
        for j in range(1,total+1):
            
            if j>= arr[i-1]:
                rem_capacity = j-arr[i-1]
                consider = dp[i-1][rem_capacity]
                
                not_consider = dp[i-1][j]
                
                dp[i][j] = consider or not_consider
            else:
                dp[i][j] = dp[i-1][j]
                
    
    vals = dp[n]
    
    min_sub_sum = float('inf')
    
    for i in range(total//2,-1,-1):
        if dp[n][i]:
            min_sub_sum = total - (2*i)
            break
    
    return min_sub_sum


a = [3, 1, 4, 2, 2, 1]
n = len(a)

print(minimum_subset_sum_difference(a,n))