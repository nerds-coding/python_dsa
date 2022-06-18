class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)


# ----------------- LEFT View -----------------
def left_view_util(root, level, level_val):

    if not root:
        return

    if not level.get(level_val):
        level[level_val] = root.data

    # using pre_order property
    left_view_util(root.left, level, level_val + 1)
    left_view_util(root.right, level, level_val + 1)


def left_view(root):
    level = dict()

    level[0] = root.data

    left_view_util(root, level=level, level_val=0)

    for i in level.values():
        print(i)


left_view(root)


# ----------------- RIGHT View -----------------
def right_view_util(root, level, level_val):

    if not root:
        return

    if not level.get(level_val):
        level[level_val] = root.data

    # using post_order property
    right_view_util(root.right, level, level_val + 1)
    right_view_util(root.left, level, level_val + 1)


def right_view(root):
    level = dict()

    level[0] = root.data

    left_view_util(root, level=level, level_val=0)

    for i in level.values():
        print(i)


right_view(root)
