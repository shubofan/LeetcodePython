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

    def longestConsecutive(self, root):
        self.res = 1

        def dfs(cur, parent, l):
            if not cur:
                return
            if parent and cur.val == parent.val + 1:
                l += 1
                self.res = max(l, self.res)
            else:
                l = 1

            dfs(cur.left, cur, l)
            dfs(cur.right, cur, l)

        dfs(root, None, 1)
        return self.res
