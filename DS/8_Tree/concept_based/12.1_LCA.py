def lowestCommonAncestor(root, p, q):

    # If looking for me, return myself
    if root == p or root == q:
        return root

    left = right = None
    # else look in left and right child
    if root.left:
        left = lowestCommonAncestor(root.left, p, q)
    if root.right:
        right = lowestCommonAncestor(root.right, p, q)

    # if both children returned a node, means
    # both p and q found so parent is LCA
    if left and right:
        return root
    else:
        # either one of the chidren returned a node,
        # meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child,
        # right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont
        # need to search all the way,
        # because in such scenarios, node where 'p' found is LCA
        return left or right
