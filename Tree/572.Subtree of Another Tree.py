# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
		def isSame(root1, root2):
			if not root1 and not root2:
				return True
			elif root1 and not root2 or root2 and not root1:
				return False
			else:
				return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2.right)

		stack = [root]
		while stack:
			cur = stack.pop()
			if isSame(cur, subRoot):
				return True
			if cur.left:
				stack += [cur.left]
			if cur.right:
				stack += [cur.right]
		return False