class Solution:

    # to check that current position of Knight is on/inside the
    # chess box
    def is_valid(self, r, c, n, visited):
        if r < 0 or c < 0 or r >= n or c >= n or visited[r][c]:
            return False

        return True

    # 1-Based Indexing
    def minStepToReachTarget(self, KnightPos, TargetPos, n):
        steps = 0
        sx = KnightPos[0] - 1
        sy = KnightPos[1] - 1

        tg_x = TargetPos[0] - 1
        tg_y = TargetPos[1] - 1

        # if the src and target is same then 0 steps
        if sx == tg_x and sy == tg_y:
            return 0

        # all the possible moves of knight
        moves_x = [1, 1, -1, -1, 2, -2, 2, -2]
        moves_y = [2, -2, 2, -2, 1, 1, -1, -1]

        # Reason to make visited matrix same as chess
        # 1- So we don't come back to from where we started
        # 2- So we don't fall in infinte call and
        # moving back and forth on same position

        # to count the visited we need chess like visited list
        # x and y
        visited = [[False for _ in range(n)] for _ in range(n)]

        # Append the SRC in Q and marking as visited
        q = list()
        q.append([sx, sy])
        visited[sx][sy] = True

        # BFS
        while q:
            size = len(q)

            steps += 1

            while size:
                # the current position of Knight
                cur_x, cur_y = q.pop(0)
                # now from current position
                # we need to find all its possible 8 moves
                # and if any of it's 8 moves is valid
                # we will store in Q
                # we can find new position valid moves
                for i in range(8):

                    # now make all the possible co-ordinates
                    # from current moves
                    new_x = cur_x + moves_x[i]
                    new_y = cur_y + moves_y[i]

                    # if in the middle found return the Steps
                    if new_x == tg_x and new_y == tg_y:
                        return steps

                    if self.is_valid(new_x, new_y, n, visited):
                        visited[new_x][new_y] = True
                        q.append([new_x, new_y])

                size -= 1

        return steps
