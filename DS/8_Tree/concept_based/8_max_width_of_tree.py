# https://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/


# similar logic as vertical order traversal
# but simply checking the length of each key's value
# and returning the max length only


def max_width_of_tree(root):

    q = list()

    lvl = dict()
    ans = 0
    q.append((0, root))

    while q:

        cur = q.pop(0)

        if not lvl.get(cur[0]):
            lvl[cur[0]] = [cur[1]]
        else:
            lvl[cur[0]].append(cur[1])

        if cur[1].left:
            q.append((cur[0] + 1, cur[1].left))

        if cur[1].right:
            q.append((cur[0] + 1, cur[1].right))

    for vals in lvl.values():
        ans = max(ans, len(vals))

    return vals
