class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time O(N^2) , for each node, check if this node is a root of BST which toke O(N)
# class Solution:
# 	def largestBSTSubtree(self, root:TreeNode) -> int:
# 		if not root:
# 			return 0
# 		if self.isBST(root, -float('inf'), float('inf')):
# 			return self.largestBSTSubtree(root.left) + self.largestBSTSubtree(root.right) + 1
# 		return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
#
# 	def isBST(self, root: TreeNode, _min, _max) -> bool:
# 		if not root:
# 			return True
# 		if root.val >= _max or root.val <= _min:
# 			return False
# 		return self.valid(root.left, _min, root.val) and self.valid(root.right, root.val, _max)

# Time O(N), each TreeNode just visited one time
class Solution1:
    def largestBSTSubtree(self, root:TreeNode) -> int:
        res = self.helper(root);
        return res[2];
    # post order traversal
    def helper(self, root) -> tuple: # return a tuple for root (max, min, number of node in BST)
        INT_MAX, INT_MIN = float('inf'),  -float('inf')

        if not root:
            return (INT_MAX, INT_MIN, 0);

        l = self.helper(root.left)
        r = self.helper(root.right)
        # if root the a BST root
        if root.val > l[1] and root.val < r[0]:
            return (min(root.val, l[0]), max(root.val, r[1]), l[2] + r[2] + 1)
        else:
            return (INT_MIN, INT_MAX, max(l[2], r[2]));
