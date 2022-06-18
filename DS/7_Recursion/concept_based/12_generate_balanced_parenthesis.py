# https://leetcode.com/problems/generate-parentheses/


def generateParenthesis(n):

    bo = n  # bo = bracket open
    bc = n  # bc = bracket close

    ans = list()

    brackets = ""

    def utils(bo, bc, ans, brackets):

        if bo == 0 and bc == 0:
            ans.append(brackets)
            return

        if bo != 0:
            brackets_opens = brackets
            brackets_opens += "("

            utils(bo - 1, bc, ans, brackets_opens)

        if bc > bo:
            brackets_close = brackets
            brackets_close += ")"
            utils(bo, bc - 1, ans, brackets_close)

    utils(bo, bc, ans, brackets)
    return ans
