# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Traverse binary tree in-order to get sorted array
# The problem become 108. Convert Sorted Array to Binary Search Tree

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.lst = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.lst += [root.val]
            inorder(root.right)

        def build(l, r):
            if l > r:
                return
            mid = (l + r) // 2
            root = TreeNode(self.lst[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        inorder(root)
        n = len(self.lst)
        l, r = 0, n - 1
        return build(l, r)