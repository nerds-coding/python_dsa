# https://practice.geeksforgeeks.org/problems/number-of-unique-paths5339/1


class Solution:
    path = [0]

    # DFS Approach
    def unique_path(self, cur_row, cur_col, row, col, grid):

        if (
            (cur_row < 0 or cur_row >= row)
            or (cur_col < 0 or cur_col >= col)
            or grid[cur_row][cur_col] != 1
        ):
            return

        if cur_row == row - 1 and cur_col == col - 1:
            self.path[0] += 1
            return

        grid[cur_row][cur_col] = -1

        self.unique_path(cur_row + 1, cur_col, row, col, grid)
        self.unique_path(cur_row, cur_col + 1, row, col, grid)

        grid[cur_row][cur_col] = 1

    # Another Approach to solve the Prob
    # https://discuss.geeksforgeeks.org/comment/da98f22819dad36871b1af6b3de88be5
    def real_unique_path(self, row, col):

        # if we have one row then we have only one unique path
        # same for the col
        if row == 1 or col == 1:
            return 1

        return self.real_unique_path(row - 1, col) + self.real_unique_path(row, col - 1)

    # Function to find total number of unique paths.
    def NumberOfPaths(self, a, b):
        # grid = [[1 for _ in range(b)] for _ in range(a)]

        # self.unique_path(0,0,a,b,grid)

        # return self.path[0]

        return self.real_unique_path(a, b)
