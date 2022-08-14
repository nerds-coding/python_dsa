"""
https://practice.geeksforgeeks.org/problems/check-for-bst/1?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions

 as we know inorder = LNR
 where in binary search tree 
 left will always will be smaller then root_node
 and 
 right will always be greater than root_node
 and thus it will give us the sorted list


"""


def inorder(self, root, ans):
    if not root:
        return

    self.inorder(root.left, ans)
    ans.append(root.data)
    self.inorder(root.right, ans)


# Function to check whether a Binary Tree is BST or not.
def isBST(self, root):

    if not root:
        return

    ans = list()

    self.inorder(root, ans)

    for i in range(1, len(ans)):
        if ans[i] < ans[i - 1]:
            return False

    return True
