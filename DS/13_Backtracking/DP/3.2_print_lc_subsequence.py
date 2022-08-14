def print_lc_subsequence(str1, str2, str1_len, str2_len, lcs):

    if str1_len == 0 or str2_len == 0:
        return

    if str1[str1_len - 1] == str2[str2_len - 1]:
        lcs.add(str1[str1_len-1])
        print_lc_subsequence(str1, str2, str1_len - 1, str2_len - 1, lcs)
    else:
        print_lc_subsequence(str1, str2, str1_len - 1, str2_len, lcs)
        print_lc_subsequence(str1, str2, str1_len, str2_len - 1, lcs)


str1 = "abcdef"
str2 = "abceg"

str1_len = len(str1)
str2_len = len(str2)
lcs = set()
print_lc_subsequence(str1, str2, str1_len, str2_len, lcs)
print(lcs)
