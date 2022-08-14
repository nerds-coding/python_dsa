# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# https://towardsdatascience.com/tackling-jump-game-problems-leetcode-e0a718e7dfba


def jump_game_forward_method(arr):
    max_reach = 0
    i = 0
    n = len(arr)

    # to check whether we don't go list out of range and
    # if we encounter zero at any index from where
    # we can't jump anywhere i<= max_reach
    while (i < n and i <= max_reach):
        max_reach = max(i + arr[i], max_reach)
        i += 1

    return i == n


# print(jump_game_forward_method([2, 3, 1, 1, 4]))


def jump_game_backward_method(arr):
    back_idx = 0

    for i in range(len(arr) - 1, -1, -1):
        if (i + arr[i] >= back_idx):
            # check whether current_idx + value of Curr_idx is
            # able to make bigger jump the back_idx
            back_idx = i
    return back_idx == 0


print(jump_game_backward_method([2, 2, 1, 0, 4]))
