class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Implementation:
    def insert(self, root, val):

        if not root:
            return Node(val)

        if root.val > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def rights_left_most_val(self, root):

        while root.left:
            root = root.left

        return root

    def delete(self, root, val):

        if root.val > val:
            root.left = self.delete(root.left, val)
        elif root.val < val:
            root.right = self.delete(root.right, val)
        else:

            if not root.left:
                temp = root
                root = temp.right

                return root

            if not root.right:
                temp = root
                root = temp.left
                return root

            temp = self.rights_left_most_val(root.right)

            temp1 = root

            root = temp

            root.right = self.delete(temp1.right, temp.val)

        return root

    def search(self, root, val):

        if root.val == val:
            return root

        if not root:
            return

        if root.val > val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(" ", root.val, end=" ")
            self.inorder(root.right)

    def iterative(self, root):
        stack = list()

        stack.append([root, 1])

        inorder = pre = post = ""
        while stack:

            if stack[-1][1] == 1:
                pre += str(stack[-1][0].val) + " "

                stack[-1][1] += 1

                if stack[-1][0].left:
                    stack.append([stack[-1][0].left, 1])
            elif stack[-1][1] == 2:
                inorder += str(stack[-1][0].val) + " "

                stack[-1][1] += 1

                if stack[-1][0].right:
                    stack.append([stack[-1][0].right, 1])
            else:
                post += str(stack[-1][0].val) + " "

                stack.pop()

        print("Pre-order -> ", pre)
        print("In-order ->", inorder)
        print("Post-order ->", post)


root = Node(6)

bst = Implementation()
bst.insert(root, 5)
bst.insert(root, 4)
bst.insert(root, 3)
bst.insert(root, 2)
bst.insert(root, 1)


bst.insert(root, 7)
bst.insert(root, 8)
bst.insert(root, 9)
bst.insert(root, 10)


bst.inorder(root)
print()

bst.iterative(root)

print(bst.search(root, 2).val)
