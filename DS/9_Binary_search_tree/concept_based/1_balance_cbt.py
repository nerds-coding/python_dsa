inorder = list()


def balanced(start, end):

    if start > end:
        return

    mid = (start + end) // 2

    node = Node(inorder[mid])

    node.left = balanced(start, mid - 1)
    node.right = balanced(mid + 1, end)

    return node
