# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         res = 0

#         if not root:
#             return res
#         cur = root
#         stack = []

#         while stack or cur:
#             while cur:
#                 stack += [cur]
#                 cur = cur.left

#             cur = stack.pop()
#             if cur.val > high:
#                 return res
#             elif cur.val >= low:
#                 res += cur.val
#             cur = cur.right


#         return res

class Solution:
	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		res = 0

		if not root:
			return res

		if root.val < low:
			return self.rangeSumBST(root.right, low, high)

		if root.val > high:
			return self.rangeSumBST(root.left, low, high)

		return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


