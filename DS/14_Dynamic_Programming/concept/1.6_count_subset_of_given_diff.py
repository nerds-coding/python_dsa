
def count_subset_of_given_diff(arr,diff):
    n = len(arr)
    total = sum(arr)
    target = (diff+total)//2
    
    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]  = 1
    
    for j in range(1,target+1):
        dp[0][i] = 0
    
    
    for i in range(1,n+1):
        for j in range(1,target+1):
            
            not_consider = dp[i-1][j]
            
            if j>=arr[i-1]:
                
                remCapacity = j-arr[i-1]
                consider = dp[i-1][remCapacity]
                
                dp[i][j] = consider+not_consider
            else:
                dp[i][j] = not_consider
    
    return dp[n][target]


arr = [1,1,2,3]

print(count_subset_of_given_diff(arr,1))