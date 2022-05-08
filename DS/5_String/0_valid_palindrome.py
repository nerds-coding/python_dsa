# https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.valid(i + 1, j, s) or self.valid(i, j - 1, s)

        return True

    def valid(self, i, j, s):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True


print(Solution().validPalindrome(s="abca"))
