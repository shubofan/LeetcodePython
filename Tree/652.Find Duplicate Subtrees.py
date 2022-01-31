# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity: O(N2), where N is the number of nodes in the tree. We visit each node once, but each creation of serial may take O(N) work.
# Space Complexity: O(N2), the size of count .

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.res = []
        self.count = {}
        self.serializeSubtree(root)

        return self.res

    def serializeSubtree(self, root: TreeNode) -> str:
        if not root:
            return '$'
        # serialized string from certain node
        s = str(root.val) + ',' + self.serializeSubtree(root.left) + ',' + self.serializeSubtree(root.right)

        if s not in self.count:
            self.count[s] = 1
        # Just put root to res one time
        elif self.count[s] == 1:
            self.res += [root]
            self.count[s] = self.count[s] + 1
        else:
            self.count[s] = self.count[s] + 1
        return s
