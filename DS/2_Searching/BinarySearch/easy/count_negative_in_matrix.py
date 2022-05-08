# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/


def countNegatives(arr):
    ans = 0

    row, col = 0, len(arr[0]) - 1
    i, j = 0, len(arr[0]) - 1
    n = len(arr)

    while (i >= 0 and i < n) and (j <= col and j >= 0):
        if arr[i][j] < 0:
            ans += n - i
            j -= 1
        else:
            i += 1
    return ans


arr = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

print(countNegatives(arr))
