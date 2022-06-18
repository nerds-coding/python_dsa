# https://www.youtube.com/watch?v=Vn2v6ajA7U0

# is similar as the previous problem but find the unique subsets

# Approach 1
def subsetsWithDup(nums):
    res = []

    ans = []

    nums = sorted(nums)

    def dfs(i):

        if i >= len(nums):
            if not ans in res:
                res.append(ans.copy())
            return

        ans.append(nums[i])
        dfs(i + 1)

        ans.pop()
        dfs(i + 1)

    dfs(0)

    return res


# Approach 2 which is quite faster than above
# b'coz "in" take extra O(n) time

def subsetsWithDup(nums):
    res = []

    ans = []

    nums = sorted(nums)

    def dfs(i):

        if i >= len(nums):
            res.append(ans.copy())
            return

        ans.append(nums[i])
        dfs(i + 1)

        ans.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)

    dfs(0)

    return res
