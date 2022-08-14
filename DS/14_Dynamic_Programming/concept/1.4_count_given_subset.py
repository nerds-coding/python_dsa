def count_subset_sum(arr, val, n):

    dp = [[1 for _ in range(val + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, val + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        """
        why j starts from 0 becoz in a
        given array we might have an element 0
        which might gets missed out in case
        when j starts from 1

        """
        for j in range(val + 1):

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

                dp[i][j] = consider + not_consider
            else:
                take_prev_value = dp[i - 1][j]
                dp[i][j] = take_prev_value

    return dp[n][val]


arr = [2, 3, 5, 6, 8, 10]
sum = 10
n = len(arr)

print(count_subset_sum(arr, sum, n))
