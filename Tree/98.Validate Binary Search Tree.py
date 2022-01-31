# Time complexity : O(N) since we visit each node exactly once.
# Space complexity : O(N) since we keep up to the entire tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
	#     def isValidBST(self, root: TreeNode) -> bool:
	#         if not root:
	#             return True
	#         elif not root.right and not root.left:
	#             return True
	#         elif not root.left:
	#             return  self.isValidBST(root.right) and root.val < self.get_MinAndMax(root.right, float('inf'), -float('inf'))[0]
	#         elif not root.right:
	#             return self.isValidBST(root.left) and root.val > self.get_MinAndMax(root.left, float('inf'), -float('inf'))[1]
	#         else:
	#             return self.isValidBST(root.left) and self.isValidBST(root.right) and self.get_MinAndMax(root.left, float('inf'), -float('inf'))[1] < root.val< self.get_MinAndMax(root.right, float('inf'), -float('inf'))[0]

	#     def get_MinAndMax(self, root:TreeNode, min_:float, max_:float) -> (int, int):
	#         stack = [root]
	#         while stack:
	#             cur = stack.pop()
	#             max_ = max(max_, cur.val)
	#             min_ = min(min_, cur.val)
	#             if cur.left:
	#                 stack += [cur.left]
	#             if cur.right:
	#                 stack += [cur.right]
	#         return (min_, max_)

	def isValidBST(self, root: TreeNode) -> bool:
		if not root:
			return True
		return self.valid(root, -float('inf'), float('inf'))

	def valid(self, root: TreeNode, _min, _max) -> bool:
		if not root:
			return True
		if root.val >= _max or root.val <= _min:
			return False
		return self.valid(root.left, _min, root.val) and self.valid(root.right, root.val, _max)