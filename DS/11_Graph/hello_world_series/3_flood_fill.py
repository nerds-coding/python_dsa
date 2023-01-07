"""
    this problem is totally similar to
    ISLAND problem
"""


def util(r, c, row, col, image, new_color, old_color):

    if r < 0 or r >= row or c < 0 or c >= col or image[r][c] != old_color:
        return

    image[r][c] = new_color

    util(r + 1, c, row, col, image, new_color, old_color)
    util(r - 1, c, row, col, image, new_color, old_color)
    util(r, c + 1, row, col, image, new_color, old_color)
    util(r, c - 1, row, col, image, new_color, old_color)


def flood_fill(image, cur_row, cur_col, new_color):

    old_color = image[cur_row][cur_col]

    # if the given old color and new_color is same
    # then simply return the image
    if new_color == old_color:
        return image

    row = len(image)
    col = len(image[0])

    util(cur_row, cur_col, row, col, image, new_color, old_color)

    return image
