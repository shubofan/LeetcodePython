# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	#     def maxDepth(self, root: TreeNode) -> int:
	#         if not root:
	#             return 0

	#         q = collections.deque()
	#         q += [root]
	#         depth = 0
	#         while q:
	#             depth += 1
	#             size = len(q)
	#             while size > 0:
	#                 cur = q.popleft()
	#                 if cur.left:
	#                     q += [cur.left]
	#                 if cur.right:
	#                     q += [cur.right]
	#                 size -=1
	#         return depth

	def maxDepth(self, root: TreeNode) -> int:
		def helper(root):
			if not root:
				return 0
			l = helper(root.left)
			r = helper(root.right)

			return 1 + max(l, r)

		return helper(root)
