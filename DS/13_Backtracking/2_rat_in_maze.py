class Solution:
    def find_path_util(self, row, col, n, visited, maze, path, ans):

        if (
            row < 0
            or col < 0
            or row >= n
            or col >= n
            or maze[row][col] == 0
            or (row, col) in visited
        ):
            return

        if row == n - 1 and col == n - 1:
            ans.append(path)

        visited.add((row, col))

        self.find_path_util(row + 1, col, n, visited, maze, path + "D", ans)
        self.find_path_util(row, col + 1, n, visited, maze, path + "R", ans)
        self.find_path_util(row - 1, col, n, visited, maze, path + "U", ans)
        self.find_path_util(row, col - 1, n, visited, maze, path + "L", ans)

        visited.remove((row, col))

    def findPath(self, m, n):

        visited = set()
        ans = list()
        row = col = 0
        path = ""

        self.find_path_util(row, col, n, visited, m, path, ans)

        return ans


maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
print(Solution().findPath(maze, 4))
