# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.getMaxSum(root)
        return self.res

    def getMaxSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftsum = max(0, self.getMaxSum(root.left))
        rightsum = max(0, self.getMaxSum(root.right))
        # path: l - root- r, l and r is either 0(not pciked) or leftsum
        self.res = max(self.res, leftsum + rightsum + root.val)
        return root.val + max(leftsum, rightsum)
