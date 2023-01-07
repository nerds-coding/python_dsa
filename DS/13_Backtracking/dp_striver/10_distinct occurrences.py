# https://practice.geeksforgeeks.org/problems/distinct-occurrences/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
class Solution:
    def util(self, st1, n, st2, m):
        if m == 0:
            return 1

        if n == 0:
            return 0

        if st1[n - 1] == st2[m - 1]:
            consider = self.util(st1, n - 1, st2, m - 1)
            not_consider = self.util(st1, n - 1, st2, m)

            return consider + not_consider
        else:
            return self.util(st1, n - 1, st2, m)

    def sequenceCount(self, arr1, arr2):
        return self.util(arr1, len(arr1), arr2, len(arr2))
