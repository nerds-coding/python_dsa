#  https://www.geeksforgeeks.org/shortest-common-supersequence/

"""
    X = abcd, Y = xycd
    Output: 6
    Explanation: Shortest Common Supersequence
    would be abxycd which is of length 6 and
    has both the strings as its subsequences.
    
    as we can see that there is few char are commno among them
    (which we can call them lcs)
    
    so abcdxycd-(1 time common words then) = shortest common subsequence
    
    
    Length of the shortest supersequence  = 
    (Sum of lengths of given two strings) - (Length of LCS of two given strings) 

"""


def lcs(str1, str2, str1_len, str2_len):

    if str1_len == 0 or str2_len == 0:
        return 0

    if str1[str1_len - 1] == str2[str2_len - 1]:
        not_consider_both_str = lcs(str1, str2, str1_len - 1, str2_len - 1)
        return 1 + not_consider_both_str

    else:
        consider_str1 = lcs(str1, str2, str1_len, str2_len - 1)
        consider_str2 = lcs(str1, str2, str1_len - 1, str2_len)
        return max(consider_str1, consider_str2)


str1 = "geek"
str2 = "eke"

str1_len, str2_len = len(str1), len(str2)

lcs_len = lcs(str1, str2, str1_len, str2_len)


total_str = str1_len + str2_len

shortest_common_subsequence = total_str - lcs_len
print(shortest_common_subsequence)
