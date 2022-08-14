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

    # add 1 b'coz (we're calling left and right so to include the root we added 1 to it)
    both_side_height_sum = 1 + height(root.left) + height(root.right)

    max_height_from_two_factors = max(both_side_height_sum, max(only_left_diameter, only_right_diameter))

    return max_height_from_two_factors


# ================ More Optimized Code ======================
"""
EXPLAINATION



Tweak the height code with a reference max diameter which 
just updates the diameter should it be maximum than the 
current diameter.



we already know how to find height. Now what is diameter, 

its nothing  but the sum of left height, right height,1 …WHY 1???
because we can't just leave the current node, that's why. 
The whole code is just the height code with the little 
difference being the updation of diameter

"""


def diameter(self, root):

    max_diameter_from_both_height = [0]
    # self.height_of_tree(root,dia)

    def height_of_tree(root):

        if not root:
            return 0

        left_height = height_of_tree(root.left)
        right_height = height_of_tree(root.right)
        total_height = 1 + max(left_height, right_height)

        max_diameter_from_both_height[0] = max(max_diameter_from_both_height[0], 1 + left_height + right_height)

        return total_height

    height_of_tree(root)
    return max_diameter_from_both_height[0]
