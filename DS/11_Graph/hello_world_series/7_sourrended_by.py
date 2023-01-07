# https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1

"""
    Approach is very simple

    instead of going from inside and making a inner DFS

    we can observe that if there is any O at boundry/corner
    and any to O is attached to that O
    then definitely they can't be convert to X

    thus we first conver that boundry/corner O and attached O  = B
    *(by making a simple DFS call like flood fill)

    and after converting all the boundry O to B
    then we finally convert the remaning O to X

    and convert the B back to O
"""


class Solution:

    # simple Island problem technique
    def dfs(self, r, c, row, col, grid):

        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != "O":
            return

        grid[r][c] = "B"

        self.dfs(r - 1, c, row, col, grid)
        self.dfs(r + 1, c, row, col, grid)
        self.dfs(r, c + 1, row, col, grid)
        self.dfs(r, c - 1, row, col, grid)

    def fill(self, n, m, mat):

        # calling for the ROW
        for i in range(n):
            # first side of the boundry
            if mat[i][0] == "O":
                self.dfs(i, 0, n, m, mat)

            if mat[i][m - 1] == "O":
                self.dfs(i, m - 1, n, m, mat)

        # calling for the COLUMNs
        for j in range(m):
            # top boundry
            if mat[0][j] == "O":
                self.dfs(0, j, n, m, mat)

            # bottom boundry
            if mat[n - 1][j] == "O":
                self.dfs(n - 1, j, n, m, mat)

        # now converting the B back to O
        # then now converting the remainging O to X
        for i in range(n):
            for j in range(m):
                if mat[i][j] == "B":
                    mat[i][j] = "O"
                elif mat[i][j] == "O":
                    mat[i][j] = "X"

        return mat
