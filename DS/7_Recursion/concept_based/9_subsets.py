# https://www.youtube.com/watch?v=REOH22Xwdkk


def subsets(nums):
    res = []

    ans = []

    def dfs(i):
        if i >= len(nums):
            # list.copy b'coz it doesn't make any changes in original array
            # b'cz list will start getting null or expand
            # so it doesn't change the original answer
            res.append(ans.copy())
            return

        ans.append(nums[i])
        dfs(i + 1)

        ans.pop()
        dfs(i + 1)

    dfs(0)
    return res


print(subsets([1, 2, 3]))
