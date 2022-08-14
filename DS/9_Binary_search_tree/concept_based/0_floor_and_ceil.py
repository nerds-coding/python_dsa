def floor_of_bst(root, key):

    ans = None

    while root:

        if root.val == key:
            return key
        # if the root is itself bigger then key
        # it cant' be the floor
        # b'coz floor is smaller
        elif root.val > key:
            root = root.left
        else:
            ans = root.val

            root = root.right

    return ans


def ceil_of_bst(root, key):

    ans = None

    while root:

        if root.val == key:
            return key
        # if the root is itself smaller then key
        # it cant' be the ceil
        # b'coz ceil is bigger possible value
        elif root.val > key:
            ans = root.val
            root = root.left
        else:
            root = root.right

    return ans
