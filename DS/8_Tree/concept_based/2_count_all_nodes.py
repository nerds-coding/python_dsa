# https://leetcode.com/problems/count-complete-tree-nodes/


def countNodes(root):
    if not root:
        return 0

    return 1 + countNodes(root.left) + countNodes(root.right)
