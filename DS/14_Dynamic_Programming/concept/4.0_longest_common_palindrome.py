#  https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1

    """
        https://www.educative.io/answers/longest-palindromic-subsequence-algorithm
        
        We can solve this problem using the solution to another similar problem - 
        the Longest Common Subsequence (LCS) problem. The idea is:

            Reverse the given sequence. Let’s call the original sequence original. 
            Let’s call the reversed sequence reverse.

            Use the LCS algorithm to find the longest common subsequence between 
            original and reverse. 
            Let LCS(original, reverse) be a function that returns the longest 
            common subsequence between the pair of strings.

            The answer from LCS will in fact be the longest palindromic subsequence.
    
    """

def longestPalinSubseq(str1):
    str2 = str1[::-1]

    len_str1 = len(str1)
    len_str2 = len(str2)
    dp = [[0 for _ in range(len_str1 + 1)] for _ in range(len_str2 + 1)]

    for i in range(1, len_str2 + 1):
        for j in range(1, len_str1 + 1):

            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len_str2][len_str1]
