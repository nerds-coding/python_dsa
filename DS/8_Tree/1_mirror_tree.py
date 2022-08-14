# https://practice.geeksforgeeks.org/problems/mirror-tree/1?page=6&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions


def mirror(root):
    q = list()

    q.append(root)

    while q:
        cur = q.pop(0)

        cur.left, cur.right = cur.right, cur.left

        if cur.left:
            q.append(cur.left)

        if cur.right:
            q.append(cur.right)

    return root
