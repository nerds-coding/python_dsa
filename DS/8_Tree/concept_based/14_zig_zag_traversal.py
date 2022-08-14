# https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions


"""
its simple BFS implementation

where each odd level is should be reversed for the zig zag traversal

"""


def zigZagTraversal(self, root):
    q = list()
    ans = list()
    odd = False

    q.append(root)

    while q:

        size = len(q)

        temp = list()

        while size:

            cur = q.pop(0)

            temp.append(cur.data)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            size -= 1

        if odd:
            temp.reverse()

        ans.extend(temp)
        odd = not odd

    return ans
