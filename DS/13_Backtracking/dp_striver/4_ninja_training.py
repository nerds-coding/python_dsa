from typing import List

# Same logic as Non adjacent problem


# reason to add value in vals
# bcz when we return 0 and then add
# in previous stack call it return the last max value not the last + cur val
# thus to avoid this we used vals
def go_ninja(cur_row, row, arr, prev, ans, vals):

    if cur_row >= row:
        return vals

    for i in range(3):
        if prev != i:
            ans[0] = max(
                go_ninja(cur_row + 1, row, arr, i, ans, vals + arr[cur_row][i]), ans[0]
            )

    return ans[0]


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    ans = [-1]

    go_ninja(0, n, points, -1, ans, 0)

    return ans[0]
