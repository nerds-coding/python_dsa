"""
    https://www.educative.io/answers/longest-palindromic-subsequence-algorithm
    
    We can solve this problem using the solution to another similar problem - 
    the Longest Common Subsequence (LCS) problem. The idea is:

        Reverse the given sequence. Let’s call the original sequence original. 
        Let’s call the reversed sequence reverse.

        Use the LCS algorithm to find the longest common subsequence between 
        original and reverse. 
        Let LCS(original, reverse) be a function that returns the longest 
        common subsequence between the pair of strings.

        The answer from LCS will in fact be the longest palindromic subsequence.

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


str1 = "GEEKSFORGEEKS"
str2 = str1[::-1]

len_str1 = len(str1)
len_str2 = len(str2)

print(lcs(str1, str2, len_str1, len_str2))
