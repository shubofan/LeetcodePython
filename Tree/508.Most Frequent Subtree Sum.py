import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.count = collections.Counter()

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.helper(root)

        maxCount = max(self.count.values())
        return [s for s in self.count if self.count[s] == maxCount]

    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = root.val + self.helper(root.left) + self.helper(root.right)
        self.count[s] += 1
        return s
