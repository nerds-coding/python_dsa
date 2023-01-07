# https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1?page=1&difficulty[]=2&status[]=unsolved&curated[]=7&sortBy=submissions


"""
    1. This question belongs to matrix chain multiplication(MCM)
     2. To solve this we need to find two points i and j     
     3. i=0 and j=n-1
     4. Now we need to find the range of k(point about which we will divide the string)
     5. our partition scheme is (i,k) and (k+1,j) so valid k's are i->j-1;
     6. Now we need to find base condition (so we would look for those i,j where our function would return 0)
     7. We will get value from each partition so we have to find min of all partition
     8. Finally memoize our solution to save time


"""

class Solution:

    dp = [[]]

    def palindrome(self, string, i, j):

        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True

    def util(self, i, j, string):
        if i >= j:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if self.palindrome(string, i, j):
            return 0

        left = right = 0
        mini = 1e9
        for k in range(i, j):

            if self.dp[i][k] != -1:
                left = self.dp[i][k]
            else:
                left = self.util(i, k, string)
                self.dp[i][k] = left

            if self.dp[k + 1][j] != -1:
                right = self.dp[k + 1][j]
            else:
                right = self.util(k + 1, j, string)
                self.dp[k + 1][j] = right

            total_partition = left + 1 + right

            mini = min(total_partition, mini)

        self.dp[i][j] = mini
        return self.dp[i][j]

    def palindromicPartition(self, string):

        n = len(string)

        self.dp = [[-1 for i in range(n + 1)] for _ in range(n + 1)]
        return self.util(0, n - 1, string)

