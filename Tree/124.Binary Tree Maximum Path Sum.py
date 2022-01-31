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
        # path: l - root - r, l and r is either 0(not picked) or leftsum
        self.res = max(self.res, leftsum + rightsum + root.val)
        return root.val + max(leftsum, rightsum)


# Time complexity: (N) where N is number of nodes, since we visit each node not more than 2 times.

# Space complexity: (H) where H is a tree height, to keep the recursion stack. In the average case of balanced tree, the tree heightH=logN,
# in the worst case of skewed tree, H=N.

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')

        def getSum(root):
            if not root:
                return 0
            max_lsum = max(0, getSum(root.left))
            max_rsum = max(0, getSum(root.right))
            self.res = max(self.res, root.val + max_lsum + max_rsum)
            return root.val + max(max_lsum, max_rsum)

        getSum(root)
        return self.res