# https://practice.geeksforgeeks.org/problems/children-sum-parent/1#


# Function to check whether all nodes of a tree have the value
# equal to the sum of their child nodes.
def isSumProperty(root):

    node = 0
    node_child = 0

    q = list()

    q.append(root)

    while q:
        cur = q.pop(0)

        # flag is used to check a node is leaf node or not
        # if it have any child node then it must be true
        flag = False
        node = cur.data
        node_child = 0

        if cur.left:
            flag = True
            q.append(cur.left)
            node_child += cur.left.data

        if cur.right:
            flag = True
            q.append(cur.right)
            node_child += cur.right.data

        if node != node_child and flag:
            return 0

    return 1
