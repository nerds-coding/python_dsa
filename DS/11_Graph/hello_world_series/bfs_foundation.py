class Solution:

    """
    Approach is opposite then what they have asked

    Instead of finding the 1 nearest for 0

    we are find the 0 for the cur 1

    bcz distance will be vice-versa
    if go from 1 to 0
    or
    0 to 1

    """

    def nearest(self, grid):

        row = len(grid)
        col = len(grid[0])

        q = list()

        visited = [[False for _ in range(col)] for _ in range(row)]

        ans = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                # storing all the 1's in the Q with distance of 0
                # 0 -> bcz 1 is very close itself so distance will
                # obvisly 0

                # also marking that 1's cell visited
                # so we don't visited that 1 in loop
                if grid[i][j] == 1:
                    q.append([[i, j], 0])
                    visited[i][j] = True

        movex = [1, -1, 0, 0]
        movey = [0, 0, 1, -1]

        while q:
            cur = q.pop(0)

            curx, cury = cur[0]
            cur_dist = cur[1]

            # updating the Ans matirx with current distance
            # we're updating ans matrix each time bcz
            # if it is in the Q then it must be
            # visited once and each step of BFS
            # we are only storing most nearest 0 to Q
            ans[curx][cury] = cur_dist
            for i in range(4):
                # checking all the 4 direction from current cell
                newX = curx + movex[i]
                newY = cury + movey[i]

                # if not visited then only put in the Q
                # and bcz to find other not visited cell
                # from that cell
                # we are reaching to 1 cell ot one time
                # so we are exploring all the cell 1 by 1
                if (
                    newX >= 0
                    and newY >= 0
                    and newX < row
                    and newY < col
                    and not visited[newX][newY]
                ):
                    visited[newX][newY] = True
                    q.append([[newX, newY], cur_dist + 1])

        return ans
