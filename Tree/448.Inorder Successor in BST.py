"""
Definition for a binary tree node.

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	"""
	@param: root: The root of the BST.
	@param: p: You need find the successor node of p.
	@return: Successor of p.
	"""
	def inorderSuccessor(self, root, p):
		pre = None

		if not root:
			return pre

		cur = root

		stack = []

		while cur or stack:
			if cur:
				stack += [cur]
				cur = cur.left

			else:
				cur = stack.pop()

				if pre == p:
					return cur
				else:
					pre = cur
					cur = cur.right
