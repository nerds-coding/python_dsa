# https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&curated[]=7&sortBy=submissions


class Solution:
    # Your task is to complete this function
    # function should return True/False or 1/0
    ans = 1

    def check_leaf_node(self, root, height, prev_height):

        if not root:
            return

        # if ans is been already initialized the n
        # direclty return false
        # no need to futher check
        # time optimization BHAI
        if self.ans == 0:
            return False

        # checking the current node is leaf or not
        if not root.left and not root.right:
            # if it is leaf node than
            # if the prev_height is -1(not been initalized)
            # then initalize the cur height till we have reached
            if prev_height[0] == -1:
                prev_height[0] = height
            else:
                # if the prev_height is been iniitalized and
                # we found that the prev_height is not same with cur height
                # it means we have found new leaf node
                # it means all the leaf node is not at same level
                # thus ans == 0(not same False)
                if prev_height[0] != height:
                    self.ans = 0

            return

        self.check_leaf_node(root.left, height + 1, prev_height)
        self.check_leaf_node(root.right, height + 1, prev_height)

    def check(self, root):

        prev_height = [-1]
        height = 0

        self.check_leaf_node(root, height, prev_height)

        return self.ans
