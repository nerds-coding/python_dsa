# https://leetcode.com/problems/word-search/

# https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
def exist(board, word):
    row = len(board)
    col = len(board[0])

    for i in range(0, row):
        for j in range(0, col):
            if(dfs(board, i, j, word)):
                return True
    return False


def dfs(board, i, j, word):
    if(len(word) == 0):
        return True

    if(i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or word[0] != board[i][j]):
        return False

    tmp = board[i][j]
    board[i][j] = "*"

    res = dfs(board, i+1, j, word[1:]) or dfs(board, i, j+1, word[1:]
                                              ) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j-1, word[1:])

    board[i][j] = tmp

    return res


print(exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
