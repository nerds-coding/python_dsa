"""
            This problem is just the modification of 
            Longest Common Subsequence problem. 
            
            The idea is to find the LCS(str, str) where, 
            str is the input string<we're taking lcs with given string but>
            
            with the restriction that when both the characters are same, 
            they shouldn’t be on the same index.
            (if they are on the same index if mean there is no repeating character
            
            we are here to find the max number of repeating chars in given string)

        Algorithm:

        Step 1: Initialize the input string, which is to be checked.

        Step 2: Initialize the length of string to the variable.

        Step 3: Create a DP table using 2D matrix and set each element to 0.

        Step 4: Fill the table if  characters are same and indexes are different.

        Step 5: Return the values inside the table

        Step 6: Print the String.

"""


def longest_repeating_subsequence(str1):

    n = len(str1)

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str1[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


str1 = "aabbcdd"
print(longest_repeating_subsequence(str1))
