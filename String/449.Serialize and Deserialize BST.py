# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
	# NO need to represent None by checking range , -> make it compact
	def serialize(self, root: TreeNode) -> str:
		"""Encodes a tree to a single string.
		"""
		self.res = []
		self.postorder(root)
		return ','.join(self.res)

	# use post order so the last element will always be root
	def postorder(self, root):
		if not root:
			return
		self.postorder(root.left)
		self.postorder(root.right)
		self.res += [str(root.val)]

	def deserialize(self, data: str) -> TreeNode:
		"""Decodes your encoded data to tree.
		"""

		def helper(lst, lower, upper):

			# if not lst or the last element not in the range, don't create node
			if not lst or lst[-1] > upper or lst[-1] < lower:
				return

			root = TreeNode(lst.pop())

			root.right = helper(lst, root.val, upper)
			root.left = helper(lst, lower, root.val)

			return root

		if not data:
			return None

		# covert data string to list of int: '2,1,3' -> [2, 1, 3]
		lst = [int(x) for x in data.split(',')]

		return helper(lst, -float('inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans