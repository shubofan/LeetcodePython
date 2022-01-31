"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        self.res = -float('inf') # maximum average
        self.node = root # node
        def helper(root): # return (sum , total_count)
            if not root:
                return (0, 0)
            l_sum, l_count = helper(root.left)
            r_sum, r_count = helper(root.right)
            if (l_sum + root.val + r_sum)/(1+l_count+r_count) > self.res:
                self.node = root
                self.res = (l_sum + root.val + r_sum)/(1+l_count+r_count)

            return (l_sum + root.val + r_sum,1+l_count+r_count)
        helper(root)
        return self.node
