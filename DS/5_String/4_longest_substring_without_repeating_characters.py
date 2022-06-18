# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is
a subsequence and not a substring.

"""

# Just 2 pointer approach
# one ptr move and insert the value and other check for the uniqueness


def lengthOfLongestSubstring(s):
    p1 = 0
    p2 = 0

    vals = set()
    max_val = 0

    while p2 < len(s):
        if not s[p2] in vals:
            vals.add(s[p2])
            p2 += 1
            max_val = max(len(vals), max_val)
        else:
            vals.remove(s[p1])
            p1 += 1

    return max_val


print(lengthOfLongestSubstring(s="pwwkew"))
