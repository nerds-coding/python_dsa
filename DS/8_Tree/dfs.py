import queue


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


# ------------------- iterative -----------------
# for the recursice we have
# inorder, preorder and postorder


def iterative_dfs(root):

    stack = list()

    stack.append(root)
    ans = list()
    while stack:

        cur_node = stack.pop()

        ans.append(cur_node.val)

        if cur_node.right:
            stack.append(cur_node.right)

        if cur_node.left:
            stack.append(cur_node.left)

    for i in ans:
        print(i)


iterative_dfs(root)
