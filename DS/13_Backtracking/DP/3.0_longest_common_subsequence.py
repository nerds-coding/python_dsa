# https://www.techiedelight.com/longest-common-subsequence/


def lcs(str1, str2, str1_len, str2_len):

    if str1_len == 0 or str2_len == 0:
        return 0

    if str1[str1_len - 1] == str2[str2_len - 1]:

        """

        at given len we found the matching char/subsequence

        so we don't need to check any of the str's char/subsequence again
        so moving form there to next chars

        """

        not_consider_both_str = lcs(str1, str2, str1_len - 1, str2_len - 1)
        return 1 + not_consider_both_str

    else:

        """

        As we don't found any matching char
        so we try to maked choice

        considering the str1 - unmatched value and not considering the str2 char

        considering the str2 - unmatched value and not considering the str1 char

        """

        consider_str1 = lcs(str1, str2, str1_len, str2_len - 1)
        consider_str2 = lcs(str1, str2, str1_len - 1, str2_len)
        return max(consider_str1, consider_str2)


str1 = "abcdefgh"
str2 = "abcegh"

print(lcs(str1, str2, len(str1), len(str2)))


def lcs_memoization(str1, str2, str1_len, str2_len, memo_dp):

    if str1_len == 0 or str2_len == 0:
        return 0

    if memo_dp[str2_len][str1_len] != -1:
        return memo_dp[str2_len][str1_len]

    else:
        if str1[str1_len - 1] == str2[str2_len - 1]:

            """

            function working is same only difference is
            storing the value in memoization dp and then returning the

            same cell value from the memoization dp

            """

            not_consider_both_str = lcs_memoization(str1, str2, str1_len - 1, str2_len - 1, memo_dp)

            memo_dp[str2_len][str1_len] = 1 + not_consider_both_str
            return memo_dp[str2_len][str1_len]

        else:
            consider_str1 = lcs_memoization(str1, str2, str1_len, str2_len - 1, memo_dp)
            consider_str2 = lcs_memoization(str1, str2, str1_len - 1, str2_len, memo_dp)
            memo_dp[str2_len][str1_len] = max(consider_str1, consider_str2)
            return memo_dp[str2_len][str1_len]


str1 = "abcdefgh"
str2 = "abcegh"

str1_len = len(str1)
str2_len = len(str2)

memo_dp = [[-1 for _ in range(str1_len + 1)] for _ in range(str2_len + 1)]

print(lcs_memoization(str1, str2, str1_len, str2_len, memo_dp))
