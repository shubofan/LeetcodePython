"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        self.res = 0
        def helper(root):
            if not root:
                return (0, 0)
            # longest consecutive increaseing sequence path
            increment = 0
            # longest consecutive decreaseing sequence path
            decrement = 0
            if root.left:
                l_increment, l_decrement = helper(root.left)
                if root.left.val + 1 == root.val:
                    increment = l_increment + 1
                if root.left.val - 1 == root.val:
                    decrement = l_decrement + 1

            if root.right:
                r_increment, r_decrement = helper(root.right)
                if root.right.val + 1 == root.val:
                    increment = max(increment, r_increment + 1)
                if root.right.val - 1 == root.val:
                    decrement = max(decrement, r_decrement + 1)

            self.res = max(self.res, increment+decrement+1)
            return (increment, decrement)
        helper(root)
        return self.res



