# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step


class Solution:
    def sumSubarrayMins(self, arr):
        # mod is b'coz if the result increase certain big integer
        n, mod = len(arr), 10 ** 9 + 7

        left, right, s1, s2 = [0] * n, [0] * n, [], []

        # getting number of element strictly
        # larger than A[i] on Left.
        for i in range(n):
            count = 1

            # get elements from stack until
            # element greater than A[i] found
            while s1 and s1[-1][0] > arr[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([arr[i], count])

        # getting number of element
        # larger than A[i] on Right.
        for i in range(n)[::-1]:
            count = 1

            # get elements from stack until
            # element greater or equal to A[i] found
            while s2 and s2[-1][0] >= arr[i]:
                count += s2.pop()[1]

            right[i] = count
            s2.append([arr[i], count])
        # calculating required result and returning it
        return sum(a * l * r for a, l, r in zip(arr, left, right)) % mod
