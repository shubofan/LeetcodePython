# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N), where N is the total number of nodes in the given tree. We visit each node at most once.

# Space Complexity: O(N). Even though we don't explicitly use any additional memory, the call stack of our recursion could be as large as the number of nodes in the worst case.
class Solution:
	def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

		if not root:
			return
		# discard left subtree
		if root.val < low:
			return self.trimBST(root.right, low, high)

		# discard right subtree
		if root.val > high:
			return self.trimBST(root.left, low, high)

		# in the range
		l = self.trimBST(root.left, low, high)
		r = self.trimBST(root.right, low, high)
		root.left = l
		root.right = r

		return root