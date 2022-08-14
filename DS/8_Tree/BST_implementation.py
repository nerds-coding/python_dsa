class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BSTOperation:
    def insert(self, val, root):
        if not root:
            return Node(val)

        if root.val > val:
            root.left = self.insert(val, root.left)
        else:
            root.right = self.insert(val, root.right)

        # reason to return the root node in TREE or LL in last
        # is b'coz when we traverse back to stack to the
        # left or right node we make sure their corresponding nodes(left or right)
        # should become the parent(which is technically left/ right node or any other root)

        # if we don't make return the root it will attach directly in root node
        # b'coz there is not node will store in stack as left or right
        # simply only base root will be sotored and its just root node
        # we are not maintaining any node in stack
        return root

    def inorder_delete(self, root):
        while root.left:
            root = root.left

        return root

    def delete_node(self, root, val):
        if root.val > val:
            root.left = self.delete_node(root.left, val)
        elif root.val < val:
            root.right = self.delete_node(root.right, val)
        else:
            if not root.left:
                temp = root
                root = temp.right
                return root

            if not root.right:
                temp = root
                root = temp.left
                return root

            # find the inorder leaf node from current right node
            # which we're considering the currenlty root node
            temp = self.inorder_delete(root.right)
            temp1 = root
            root = temp

            # after adding the new node
            # now we are attaching the new right node from where we left
            # where temp1 is next right node which be get attached to right
            root.right = self.delete_node(temp1.right, temp.val)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)


root = Node(6)

bst = BSTOperation()

bst.insert(5, root)
bst.insert(7, root)
bst.insert(4, root)
bst.insert(8, root)
bst.insert(3, root)
bst.insert(9, root)


bst.inorder(root)

bst.delete_node(root, 4)

print()
print("After deletion of node ")
bst.inorder(root)
