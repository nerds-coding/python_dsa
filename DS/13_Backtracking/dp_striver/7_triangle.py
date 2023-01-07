# https://leetcode.com/problems/triangle/solutions/2146264/c-python-simple-solution-w-explanation-recursion-dp/


class Solution:
    def util(self, i, j, triangle):

        if i == len(triangle):
            return 0

        down = self.util(i + 1, j, triangle) + triangle[i][j]
        right = self.util(i + 1, j + 1, triangle) + triangle[i][j]

        return min(down, right)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.util(0, 0, triangle)
