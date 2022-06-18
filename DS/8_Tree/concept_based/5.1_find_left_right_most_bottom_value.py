# https://leetcode.com/problems/find-bottom-left-tree-value/

# https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-%2B-Java)


def findBottomLeftValue(root):

    # whenever we are going for BFS alway use Iterative WAY
    q = list()

    q.append(root)
    cur = None
    while q:

        cur = q.pop(0)

        # reason to go first right
        # b'cz we're using Q and
        # in the last the left side node
        # will be in the CUR variable
        # which will be technially the left most bottom value
        if cur.right:
            q.append(cur.right)

        if cur.left:
            q.append(cur.left)

        # by changing the left to first we can get
        # right most bottom value also
    return cur.val
