"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
	"""
	@param root: the given BST
	@param target: the given target
	@return: the value in the BST that is closest to the target
	"""

	def closestValue(self, root, target):

		def helper(root, target):
			if not root:
				return
			if abs(root.val - target) < abs(self.closet.val - target):
				self.closet = root

			if target < root.val:
				helper(root.left, target)

			if target > root.val:
				helper(root.right, target)

		self.closet = root
		helper(root, target)
		return self.closet.val