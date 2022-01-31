# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         def helper(root): # return (LongestZigZagPath of its left, LongestZigZagPath of its right)
#             if not root:
#                 return (0, 0)
#             ll,lr = helper(root.left)
#             rl,rr = helper(root.right)
#             self.res = max(self.res, 1 + max(rl, lr))
#             return (1+lr, 1+rl) #

#         self.res = 0
#         helper(root)
#         return self.res - 1

class Solution:
	def longestZigZag(self, root: Optional[TreeNode]) -> int:
		def helper(root, isLeft):  # return (LongestZigZagPath of root)
			if not root:
				return 0
			l = helper(root.left, True)
			r = helper(root.right, False)
			self.res = max(self.res, 1 + max(l, r))
			if isLeft:
				return 1 + r
			else:
				return 1 + l

		self.res = 0
		helper(root, False)
		return self.res - 1