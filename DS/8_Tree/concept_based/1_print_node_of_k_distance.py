# https://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/

# ----- Iterative -----
# space O(n) and Time O(n)
# we are using BFS and extra Dict to store the LEVEL
def print_k_distance(root, k):
    q = list()
    level = dict()

    q.append(root)

    level[q[0]] = 0

    while q:
        cur = q.pop(0)
        cur_level = level[cur]

        if cur.left:
            level[cur.left] = cur_level + 1
            q.append(cur.left)

        if cur.right:
            level[cur.right] = cur_level + 1
            q.append(cur.right)

        if cur_level == k:
            print(cur.val)


# ----- Recursive -----
# space O(1) and Time O(n)
def print_k_distance_recursive(root, k):

    if not root:
        return

    if not k:
        print(root.val)

    print_k_distance_recursive(root.left, k - 1)
    print_k_distance_recursive(root.right, k - 1)
