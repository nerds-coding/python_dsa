# https://www.geeksforgeeks.org/find-maximum-or-minimum-in-binary-tree/


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def max_in_tree(root, val=-1):
    if not root:
        return val  # simply returning the previous data

    # root.data is current root value
    # and along with current value we are calling the next element
    # thus data is previous

    return max(
        val, max(max_in_tree(root.left, root.data), max_in_tree(root.right, root.data))
    )


if __name__ == "__main__":
    root = newNode(11)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(76)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(1)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)

    # Function call
    print("Maximum element is", max_in_tree(root))
