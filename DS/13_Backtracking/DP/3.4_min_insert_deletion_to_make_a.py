# https://www.geeksforgeeks.org/minimum-number-deletions-insertions-transform-one-string-another/

"""
        Algorithm: 

    str1 and str2 be the given strings.
    m and n be their lengths respectively.
    len be the length of the longest common subsequence of str1 and str2
    minimum number of deletions minDel = m – len
    minimum number of Insertions minInsert = n – len
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


str1 = "heap"
str2 = "pea"

str1_len, str2_len = len(str1), len(str2)

lcs_len = lcs(str1, str2, str1_len, str2_len)

print((str1_len - lcs_len) + (str2_len - lcs_len))
