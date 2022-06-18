def permutation(s):
    res = []
    ans = []

    def dfs(i):

        if i+1 >= len(s):
            res.append(ans.copy())
            return

        ans.append(s[i] + " " + s[i + 1 :])

        dfs(i + 1)

        ans.pop()

        dfs(i + 1)

    dfs(0)

    return res


print(permutation("abc"))
