# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
	def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
		def dfs(root, depth):
			if not root:
				return
			if depth == self.max_depth:
				self.res += root.val
			if depth > self.max_depth:
				self.res = root.val
				self.max_depth = depth
			dfs(root.left, depth + 1)
			dfs(root.right, depth + 1)

		self.res = 0
		self.max_depth = 0
		dfs(root, 0)
		return self.res
# BFS
# class Solution:
#     def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

#         res = 0

#         q = collections.deque()
#         q += [root]

#         while q:
#             size = len(q)
#             level_sum = 0
#             for i in range(size):

#                 node = q.popleft()
#                 level_sum += node.val
#                 if node.left:
#                     q += [node.left]
#                 if node.right:
#                     q += [node.right]

#             res = level_sum

#         return res



