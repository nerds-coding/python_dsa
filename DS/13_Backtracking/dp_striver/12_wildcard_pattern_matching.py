# https://practice.geeksforgeeks.org/problems/wildcard-pattern-matching/1

# STRIVER bhaiya ki jai ho


class Solution:

    dp = [[]]

    def util(self, string, pattern, i, j):

        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if i == 0 and j == 0:
            return True

        if i == 0 and j > 0:
            return False

        if j == 0 and i > 0:
            for i in range(1, i + 1):
                if string[i - 1] != "*":
                    return False
            return True

        if string[i - 1] == pattern[j - 1] or string[i - 1] == "?":
            self.dp[i][j] = self.util(string, pattern, i - 1, j - 1)
            return self.dp[i][j]
        elif string[i - 1] == "*":
            matching_all_char_against_star = self.util(string, pattern, i, j - 1)
            matching_single_char_against_star = self.util(string, pattern, i - 1, j - 1)
            matching_null_char_against_star = self.util(string, pattern, i - 1, j)

            self.dp[i][j] = (
                matching_all_char_against_star
                or matching_single_char_against_star
                or matching_null_char_against_star
            )
            return self.dp[i][j]

        return False

    def wildCard(self, string, pattern):

        n = len(string)
        m = len(pattern)
        self.dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        return self.util(string, pattern, n, m)
