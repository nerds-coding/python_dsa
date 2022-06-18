# https://leetcode.com/problems/jump-game-ii/

# TLE
# def jump(nums):

#     length = len(nums)
#     cur_idx = 0
#     last = False
#     count = 0

#     while (last is not True):
#         n = nums[cur_idx]
#         new_idx = 0

#         if (n == 1):
#             cur_idx += 1
#         else:
#             tmp = 0

#             for i in range(n):
#                 if (tmp <= nums[cur_idx + i + 1]):
#                     tmp = nums[cur_idx + 1 + i]
#                     new_idx = cur_idx + 1 + i

#         if (length - 1 == new_idx):
#             return count + 1
#         else:
#             count += 1
#             cur_idx = new_idx

# print(jump([2, 3, 0, 1, 4]))


def jump(nums):
    if (len(nums) == 1):
        return 0

    maxReach = nums[0]
    steps = nums[0]
    jumps = 0

    for i in range(1, len(nums) - 1):
        maxReach = max(maxReach, i + nums[i])
        steps -= 1

        if (steps == 0):
            # if steps == 0 then it means we have exhuasted
            # all the walk we can make now we check
            # new maxReach, that how much more we can make walk

            # jump +=1, b'coz we have exhuasted maxReach so
            # now will count that as jump
            jumps += 1
            steps = maxReach - i

    # +1 b'coz we are iterating till second last element
    return jumps + 1


print(jump([2, 3, 0, 1, 4]))
