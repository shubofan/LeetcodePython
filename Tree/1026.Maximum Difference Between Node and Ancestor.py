# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
		self.res = 0

		# min_ min val along the path from parent to node
		def dfs(root, min_, max_):
			if not root:
				return
			min_ = min(min_, root.val)
			max_ = max(max_, root.val)

			self.res = max(self.res, max_ - min_)

			dfs(root.left, min_, max_)
			dfs(root.right, min_, max_)

		dfs(root, root.val, root.val)
		return self.res