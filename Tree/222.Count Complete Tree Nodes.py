# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def countNodes(self, root: TreeNode) -> int:
		if not root:
			return 0
		lh, rh = self.get_left_height(root), self.get_right_height(root)
		if lh == rh:
			return pow(2, lh) - 1
		return 1 + self.countNodes(root.left) + self.countNodes(root.right)

	def get_left_height(self, root: TreeNode) -> int:
		if not root:
			return 0
		else:
			return 1 + self.get_left_height(root.left)

	def get_right_height(self, root: TreeNode) -> int:
		if not root:
			return 0
		else:
			return 1 + self.get_right_height(root.right)
