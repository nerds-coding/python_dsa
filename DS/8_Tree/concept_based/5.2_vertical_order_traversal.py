# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# having similiar logic as top view but
# just adding each element at their corresponding level


def verticalTraversal(root):
    level = dict()

    q = list()

    ans = list()

    q.append((0, root))

    while q:

        cur = q.pop(0)

        if not level.get(cur[0]):
            level[cur[0]] = [cur[1].val]
        else:
            level[cur[0]].append(cur[1].val)

        if cur[1].left:
            q.append((cur[0] - 1, cur[1].left))

        if cur[1].right:
            q.append((cur[0] + 1, cur[1].right))

    for i in sorted(level):
        ans.append(sorted(level[i], reverse=False))

    return ans
