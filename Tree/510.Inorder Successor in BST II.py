
"""
Description:

Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

Follow up:
Could you solve it without looking up any of the node's values?
"""

class Node:
	def __init__(self):
		self.right = None
		self.left = None
		self.parent =None

class Solution:
	def inorderSuccessor(self, node: Node) -> Node:
		"""
		If the node has a right child, and hence its successor is somewhere lower in the tree.
		Go to the right once and then as many times to the left as you could. Return the node you end up with.
		"""
		if node.right:
			node = node.right
			while node.left:
				node = node.left
			return node

		"""
		Node has no right child, and hence its successor is somewhere upper in the tree. 
		Go up till the node is left child of its parent. The answer is the parent. 
		"""
		while node.parent and node.parent.right == node:
			node = node.parent
		return node.parent
