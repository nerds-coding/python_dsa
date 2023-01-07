# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1


class Solution:
    dp = [[]]

    def mcm(self, arr, i, j):

        # if both pointers r pointing to same matrix
        # it means we have one matrix then there no othere matrix with
        # whom we can multiply
        # thus it will take 0 efforts
        if i >= j:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]
        mini = 1e9

        for k in range(i, j):
            # k denote till where we can start or end
            # to make brackets

            # here from i to k we have all the matrix
            # in one bracket (which will futher get more recursive)
            first_pair_of_brackets = self.mcm(arr, i, k)

            # here from k+1 to j we have all the matrix with same brackets
            # k+1 bcz till k we are forming bracket with i
            second_pair_of_brackets = self.mcm(arr, k + 1, j)

            # above we have made 2 different types of bracket
            # we also have to add those bracket with each other
            # to get the final efforts
            # so i-1 is last row dimension
            # k = mutual row and col mixture
            # j = col of cur matrix dimension
            extra_effort = arr[i - 1] * arr[k] * arr[j]

            total_efforts = (
                first_pair_of_brackets + second_pair_of_brackets
            ) + extra_effort

            mini = min(mini, total_efforts)

        self.dp[i][j] = mini
        return self.dp[i][j]

    def matrixMultiplication(self, N, arr):
        self.dp = [[-1 for i in range(N + 1)] for _ in range(N + 1)]
        return self.mcm(arr, 1, len(arr) - 1)
