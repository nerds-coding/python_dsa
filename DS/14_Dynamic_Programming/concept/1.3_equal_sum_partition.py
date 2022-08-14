""" in this problem we have to find that given array can be divided into 
2 part such that both sub-array sum == equal to each other

so we can take total of array and divide by 2 

then we have to check that given array can make half subarray 
such that sum of that subarray = half

(just converting into the subset problem)
"""


def equal_partition(arr):

    total = sum(arr)

    if total & 1:
        return "Half cannot be found because total is odd"
    else:
        half = total // 2
        n = len(arr)

    dp = [[True for _ in range(half + 1)] for _ in range(n + 1)]

    # If sum is 0, then answer is true
    for i in range(n + 1):
        dp[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, half + 1):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, half + 1):

            if j >= arr[i - 1]:

                remaining_capacity_for_other = j - arr[i - 1]

                """
                    reason we r not adding any value here 
                    is b'coz 
                                
                    we just have to check if we 
                    consider this value in the subarray
                    then remaning (players) can make the subarray or not
                    
                    if yes then should take him 
                    (b'coz we have to return the boolean value only)
                    
                """
                consider = dp[i - 1][remaining_capacity_for_other]

                not_consider = dp[i - 1][j]

                dp[i][j] = consider or not_consider
            else:
                take_prev_value = dp[i - 1][j]
                dp[i][j] = take_prev_value

    return dp[n][half]


print(equal_partition(arr=[5, 4, 5]))
