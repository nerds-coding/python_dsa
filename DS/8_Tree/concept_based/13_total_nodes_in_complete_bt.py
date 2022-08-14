# https://leetcode.com/problems/count-complete-tree-nodes/


def countNodes(root):
    l = r = 0

    cur = root
    while cur:
        l += 1
        cur = cur.left

    cur = root
    while cur:
        r += 1
        cur = cur.right

    if l == r:
        return (2 ** l) - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)
