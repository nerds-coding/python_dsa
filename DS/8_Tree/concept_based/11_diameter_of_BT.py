def height(root):
    if not root:
        return 0

    return 1 + max(height(root.left), height(root.right))


def diameterOfBinaryTree(root):

    if not root:
        return 0

    # only_left_diameter = we can this as util fucntion
    # this function return the diameter only of the left
    # from recursion leap of faith (which store/calc  the value from the
    # returned height from the left and right side of the binary tree)
    only_left_diameter = diameterOfBinaryTree(root.left)

    only_right_diameter = diameterOfBinaryTree(root.right)

    both_side_height_sum = height(root.left) + height(root.right)

    max_height_from_two_factors = max(
        both_side_height_sum, max(only_left_diameter, only_right_diameter)
    )

    return max_height_from_two_factors
