# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time Complexity: O(N)  where N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.

# Space Complexity: O(N) This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed BST could be N.
class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		if p == root or q == root:
			return root
		if p.val < root.val < q.val or q.val < root.val < p.val:
			return root

		if p.val < root.val and q.val < root.val:
			return self.lowestCommonAncestor(root.left, p, q)
		if p.val > root.val and q.val > root.val:
			return self.lowestCommonAncestor(root.right, p, q)