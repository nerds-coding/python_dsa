# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#


def topView(self, root):

    lvl = dict()
    ans = list()

    q = list()

    depth = 0
    q.append((depth, root))

    while q:

        cur = q.pop(0)

        if not lvl.get(cur[0]):
            lvl[cur[0]] = cur[1].data

        if cur[1].left:
            q.append((cur[0] - 1, cur[1].left))

        if cur[1].right:
            q.append((cur[0] + 1, cur[1].right))

    for i in sorted(lvl):
        ans.append(lvl[i])
    return ans


# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

def bottomView(self, root):

    lvl = dict()
    ans = list()

    q = list()

    q.append((0, root))

    while q:

        cur = q.pop(0)

        lvl[cur[0]] = cur[1].data

        if cur[1].left:
            q.append((cur[0] - 1, cur[1].left))

        if cur[1].right:
            q.append((cur[0] + 1, cur[1].right))

    for i in sorted(lvl):
        ans.append(lvl[i])

    return ans
