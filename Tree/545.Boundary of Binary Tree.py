"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution(object):
	def boundaryOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

		res = []
		if not root:
			return res

		# add root
		res += [root.val]

		# add left boundary from top to down
		t = root.left
		while t:
			# add t only if t is not leaf
			if t.left or t.right:
				res.append(t.val)
			if t.left:
				t = t.left
			else:
				t = t.right

		def getLeaf(node):
			if not node.left and not node.right:
				res.append(node.val)

			if node.left:
				getLeaf(node.left)
			if node.right:
				getLeaf(node.right)

		# add add leaf
		getLeaf(root)

		stack = []
		t = root.right
		# add right boundary from down to top
		while t:
			if t.left or t.right:
				stack.append(t.val)
			if t.right:
				t = t.right
			else:
				t = t.left

		# add right boundary reversely
		while stack:
			res.append(stack.pop())

		return res