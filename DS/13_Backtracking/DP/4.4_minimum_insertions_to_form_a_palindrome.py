# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/


def min_insetion_to_make_str_palindrome(str1, str2, len_str1, len_str2):

    if not len_str1 or not len_str2:
        return 0

    if str1[len_str1 - 1] == str2[len_str2 - 1]:
        return 1 + min_insetion_to_make_str_palindrome(str1, str2, len_str1 - 1, len_str2 - 1)

    else:
        return max(
            min_insetion_to_make_str_palindrome(str1, str2, len_str1, len_str2 - 1),
            min_insetion_to_make_str_palindrome(str1, str2, len_str1 - 1, len_str2),
        )


str1 = "geeks"
n = len(str1)
str2 = str1[::-1]

# similar logic as number of deletion to make a string palindrome

# to make string palindrome we have certain amount of chars
# so instead of deleting the char we should add that same chars in original string

print(n - min_insetion_to_make_str_palindrome(str1, str2, n, n))
