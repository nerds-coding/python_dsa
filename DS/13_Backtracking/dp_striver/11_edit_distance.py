class Solution:

    dp = [[]]

    def util(self, st1, n, st2, m):

        # if there is no element left in n
        # then we have to insert m's element into n
        # thus return the count of m
        if n == 0:
            return m
        # if there is no element in m
        # then we have delete remaning element of n
        # which will cost same operation of len of n
        if m == 0:
            return n

        if self.dp[n][m] != -1:
            return self.dp[n][m]

        # if element match then there is not operation needed
        if st1[n - 1] == st2[m - 1]:
            self.dp[n][m] = 0 + self.util(st1, n - 1, st2, m - 1)
            return self.dp[n][m]
        else:
            # here we are trying all the given 3 option

            # while inserting we are asuming that we are
            # inserting at back the element which is required
            # thus we move only m not n
            # bcz n current element is ame
            insert = 1 + self.util(st1, n, st2, m - 1)

            # replace the element with required one
            # thus n-1 and m-1
            replace = 1 + self.util(st1, n - 1, st2, m - 1)

            # we are here deleting from n not from thus m stay as it is
            delete = 1 + self.util(st1, n - 1, st2, m)

            self.dp[n][m] = min(insert, replace, delete)
            return self.dp[n][m]

    def editDistance(self, s, t):
        self.dp = [[-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        return self.util(s, len(s), t, len(t))
