# https://www.geeksforgeeks.org/longest-common-substring-dp-29/


def lcs(str1, str2, str1_len, str2_len, max_len):

    if str1_len == 0 or str2_len == 0:
        return 0

    if str1[str1_len - 1] == str2[str2_len - 1]:

        # how calling the string by skipping the char which is already matched
        nxt_char = lcs(str1, str2, str1_len - 1, str2_len - 1, max_len)

        # using max_len array to store the longest substring
        # bcoz we are retruning at 0 at end
        max_len[0] = max(max_len[0], 1 + nxt_char)
        return 1 + nxt_char
    else:
        lcs(str1, str2, str1_len, str2_len - 1, max_len)
        lcs(str1, str2, str1_len - 1, str2_len, max_len)

        # returning 0 bcoz we want to find the substirng
        # if it is not continous then we start again from the zero
        return 0


str1 = "abcdef"
str2 = "abceg"

str1_len = len(str1)
str2_len = len(str2)
max_len = [-1]
lcs(str1, str2, str1_len, str2_len, max_len)
print(max_len)
