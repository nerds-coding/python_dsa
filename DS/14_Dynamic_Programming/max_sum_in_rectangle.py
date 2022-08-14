# https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1/?page=1&curated[]=8&sortBy=submissions#


# Tushar Roy Explanation is amazing

    
class Solution:
    def kadane(self, arr):

        left = right = 0

        total = float("-inf")
        new_total = 0

        for i in range(len(arr)):
            new_total += arr[i]
            if total < new_total:
                total = new_total
                left = right
                right = i

            # to new_total goes beyound 0
            # then if any new postive or negative number comes in
            # it won't be able to  start from there
            if new_total < 0:
                new_total = 0

        # return total
        return [total, (left, right)]

    def maximumSumRectangle(self, r, c, m):

        # this variable will tell about the co-ordinate in matrix
        left_from = right_from = bottom_left_till = bottom_right_till = 0

        prev_sum = float("-inf")
        prefix_sum = [0] * r
        for i in range(c):
            prefix_sum = [0] * r
            for col in range(i, c):
                for row in range(r):

                    prefix_sum[row] += m[row][col]

                new_kadane = self.kadane(prefix_sum)
                # prev_sum = max(prev_sum , self.kadane(prefix_sum))
                if new_kadane[0] > prev_sum:
                    prev_sum = new_kadane[0]

                    left_from = i
                    right_from = col

                    bottom_left_till = new_kadane[1][0]
                    bottom_right_till = new_kadane[1][1]

        return prev_sum
