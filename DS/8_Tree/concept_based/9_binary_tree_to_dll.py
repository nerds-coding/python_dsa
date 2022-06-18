# https://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/


class Solution:
    prev = None
    head = None

    def dll(self, root):
        if not root:
            return

        self.dll(root.left)

        if not self.prev:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root

        self.dll(root.right)

        return self.head

    def flatten(self, root):
        return self.dll(root)
