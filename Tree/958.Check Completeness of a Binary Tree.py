# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
	def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
		q = collections.deque()
		q += [root]
		# meet a None, everything after it should be None as well
		while q[0]:
			cur = q.popleft()
			q += [cur.left]
			q += [cur.right]
		# print(q)
		while q and not q[0]:
			q.popleft()
		# print(q)
		return len(q) == 0

# class Solution:
#     def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
#         q = collections.deque()
#         res = []
#         if not root:
#             return True

#         q += [root]
#         while q:
#             cur = q.popleft()
#             res += [cur.val]
#             if cur.val != '#':
#                 if cur.left:
#                     q += [cur.left]
#                 if not cur.left:
#                     q += [TreeNode('#')]


#                 if cur.right:
#                     q += [cur.right]
#                 if not cur.right:
#                     q += [TreeNode('#')]


#         number = False
#         # print(res)
#         for i in range(len(res) - 1, -1, -1):
#             if number and res[i] == '#':
#                 return False
#             if res[i] != '#':
#                 number = True

#         return True
