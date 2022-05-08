
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

            temp = self.inorder_delete(root.right)
            temp1 = root
            root = temp
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



# ------------------- iterative


def iterative_bfs(root):

    q = list()

    q.append(root)

    ans = list()
    while q:

        cur_node = q.pop(0)  # poping the first element
        print(cur_node.val)
        if cur_node.left:
            q.append(cur_node.left)

        if cur_node.right:
            q.append(cur_node.right)


iterative_bfs(root)
