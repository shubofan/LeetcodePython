# Definition for a binary tree node.

class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def recoverTree(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		stack = []
		cur = root
		pre = None
		errNode1 = None
		errNode2 = None
		while stack or cur:
			if cur:
				stack += [cur]
				cur = cur.left
			else:
				cur = stack.pop()
				# has not found 1st errorNode, pre exist and pre is errorNode
				if not errNode1 and pre and cur.val < pre.val:
					errNode1 = pre
				if errNode1 and pre and cur.val < pre.val:
					errNode2 = cur
				pre = cur
				cur = cur.right
		errNode1.val, errNode2.val = errNode2.val, errNode1.val

	# recursive
	def recoverTree(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		self.pre = None
		self.errNode1, self.errNode2 = None, None

		def inorder(root):
			if not root:
				return

			inorder(root.left)

			# process current node i.e. root
			if self.pre and root.val < self.pre.val:
				self.errNode2 = root
				# first swap occurence, continue to find the 2nd error Node
				if not self.errNode1:
					self.errNode1 = self.pre
				# second swap occurence
				else:
					return

			self.pre = root
			inorder(root.right)

		inorder(root)

		self.errNode1.val, self.errNode2.val = self.errNode2.val, self.errNode1.val