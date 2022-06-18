# https://leetcode.com/problems/roman-to-integer/


"""
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
"""


def romanToInt(s):
    # mapping all the possible individual roman symbols
    roman = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    # flag, b'coz to keep account of current value make
    # any Integer with prev value or not
    flag = False
    ans = 0
    for i in range(1, len(s)):
        r = roman.get(
            s[i - 1] + s[i]
        )  # check the current and prev value are present in
        # the dict, if yes,
        # then simply add them and make flag True
        # (which mean current value is already used)
        if not flag and r:
            ans += r
            flag = True
        else:
            # if prev value is already is been used then avoid adding again
            ans += roman.get(s[i - 1]) if (not flag) else 0

            # making flag false, so we can now we the prev value
            flag = False

    return ans if flag else ans + roman.get(s[-1])


print(romanToInt(s="MCMXCIV"))
