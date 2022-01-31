# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time Complexity: O(N), where N is the number of nodes in the given tree.

# Space Complexity: O(H) in additional space complexity, where H is the height of the given tree, and the size of the implicit call stack in our in-order traversal.
class Solution:
	def increasingBST(self, root: TreeNode) -> TreeNode:
		self.dummy = TreeNode(-1)
		self.cur = self.dummy

		def inorder(root):
			if not root:
				return
			inorder(root.left)

			root.left = None
			self.cur.right = root
			self.cur = root

			inorder(root.right)

		inorder(root)

		return self.dummy.right

