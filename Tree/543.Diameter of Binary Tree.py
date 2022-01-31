# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		def get_depth(root):
			if not root:
				return 0
			l_depth = get_depth(root.left)
			r_depth = get_depth(root.right)

			self.res = max(self.res, l_depth + r_depth + 1)
			return max(l_depth, r_depth) + 1

		self.res = 0
		get_depth(root)
		return self.res - 1