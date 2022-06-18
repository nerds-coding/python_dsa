# https://leetcode.com/problems/balanced-binary-tree/submissions/

# https://www.youtube.com/watch?v=QfJsau0ItOY


def isBalanced(root):
    def dfs(root):

        if not root:
            return (True, 0)

        l = dfs(root.left)
        r = dfs(root.right)

        balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

        return (balanced, 1 + max(l[1], r[1]))

    return dfs(root)[0]
