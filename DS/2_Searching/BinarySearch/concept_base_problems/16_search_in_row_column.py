# https://www.callicoder.com/binary-search-row-wise-column-wise-sorted-matrix/


def search_in_matrix(arr, x):
    i, j = 0, len(arr[0]) - 1

    while i >= 0 and j < len(arr):
        if arr[i][j] == x:
            return f"Element present at row = {i+1} and column = {j+1}"
        elif arr[i][j] > x:
            j -= 1
        else:
            i += 1

    return -1


arr = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]

print(search_in_matrix(arr, 29))
