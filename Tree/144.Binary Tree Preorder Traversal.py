# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		res = []
		if not root:
			return res

		stack = [root]
		while stack:
			root = stack.pop()
			res += [root.val]
			if root.right:
				stack += [root.right]
			if root.left:
				stack += [root.left]
		return res