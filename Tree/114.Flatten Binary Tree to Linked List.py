# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity: O(N) since we process each node of the tree at most twice
# Space O(1)
class Solution:
	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		if not root:
			return root
		cur = root
		while cur:
			# if it has left, find the right most node of  the left subtree
			if cur.left:
				right_most = cur.left
				while right_most.right:
					right_most = right_most.right
				right_most.right = cur.right
				cur.right = cur.left
				cur.left = None

			# For every node we check if it has a left child or not. If it doesn't we simply move on to the right hand side
			cur = cur.right
