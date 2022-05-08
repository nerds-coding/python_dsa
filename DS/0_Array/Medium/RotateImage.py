# https://www.google.com/url?q=https://leetcode.com/problems/rotate-image/&sa=D&source=editors&ust=1638965780197000&usg=AOvVaw1w8rhCoeylzEyUQAcW_mPL

def rotate(matrix):
    n = len(matrix)

    # Transpose of matrix
    for i in range(0, n):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse of matrix's row
    for i in range(0, n):
        for j in range(0, n//2):
            matrix[i][n-j-1], matrix[i][j] = matrix[i][j], matrix[i][n-j-1]

    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
