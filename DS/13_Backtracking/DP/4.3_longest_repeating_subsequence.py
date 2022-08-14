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


def longest_repeating_subseqeuence(str1, str2, len_str1, len_str2):

    if len_str1 == 0 or len_str2 == 0:
        return 0

    if str1[len_str1 - 1] == str2[len_str2 - 1] and (len_str1 != len_str2):
        return 1 + longest_repeating_subseqeuence(str1, str2, len_str1 - 1, len_str2 - 1)
    else:
        return max(
            longest_repeating_subseqeuence(str1, str2, len_str1, len_str2 - 1),
            longest_repeating_subseqeuence(str1, str2, len_str1 - 1, len_str2),
        )


str1 = "aabbcdd"

n = len(str1)

print(longest_repeating_subseqeuence(str1, str1, n, n))
