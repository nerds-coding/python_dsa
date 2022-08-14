# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions4610/0/#

# same logic to make 4.0 only subtracting with len of string
# which means removing un-wanted chars from the string


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


str1 = "aebcbda"
str2 = str1[::-1]

len_str1 = len(str1)
len_str2 = len(str2)

print(len_str1 - lcs(str1, str2, len_str1, len_str2))
