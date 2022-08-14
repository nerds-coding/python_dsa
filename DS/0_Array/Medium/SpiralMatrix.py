# problem = https://leetcode.com/problems/spiral-matrix/


# one liner = return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
# onl liner explanation - https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby

def spiralOrder(matrix):
    rowStart = 0
    rowEnd = len(matrix)
    colEnd = len(matrix[0])
    colStart = 0

    ans = list()

    while((rowStart < rowEnd) and (colStart < colEnd)):

        for i in range(colStart, colEnd):
            ans.append(matrix[rowStart][i])

        rowStart += 1

        for i in range(rowStart, rowEnd):
            ans.append(matrix[i][colEnd-1])

        colEnd -= 1

        if(colStart < colEnd):
            for i in range(colEnd-1, colStart-1, -1):
                ans.append(matrix[rowEnd-1][i])

        rowEnd -= 1

        if(rowStart < rowEnd):
            for i in range(rowEnd-1, rowStart-1, -1):
                ans.append(matrix[i][colStart])
        colStart += 1

    return ans


print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
