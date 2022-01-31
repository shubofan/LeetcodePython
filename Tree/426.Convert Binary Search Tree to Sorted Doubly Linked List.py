
"""
# Time complexity: O(N) since each node is processed exactly once.

Space complexity : O(N) We have to keep a recursion stack of the size of the tree height, which is (logN) for the best case of completely balanced tree 

and O(N) for the worst case of completely unbalanced tree. 

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
	"""
	@param root: root of a tree
	@return: head node of a doubly linked list
	"""

	# def treeToDoublyList(self, root):
	# self.first, self.pre = None, None

	# def traverseToLeftMost(root):

	#     if not root:
	#         return

	#     traverseToLeftMost(root.left)

	#     if not self.first:
	#         self.first = root
	#     elif self.pre:
	#         self.pre.right = root
	#         root.left = self.pre
	#     self.pre = root

	#     traverseToLeftMost(root.right)

	# traverseToLeftMost(root)
	# self.pre.right = self.first
	# self.first.left = self.pre
	# return self.first

	def treeToDoublyList(self, root):

		first, pre = None, None
		stack = []
		cur = root

		# Pure in-order traversal
		while cur or stack:
			if cur:
				stack += [cur]
				cur = cur.left
			else:
				cur = stack.pop()
				if not first:
					first = cur
				elif pre:
					pre.right, cur.left = cur, pre
				pre = cur
				cur = cur.right

		if first and pre:
			first.left = pre
			pre.right = first

		return first
