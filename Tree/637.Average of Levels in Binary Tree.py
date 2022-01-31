# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
		res = []
		q = collections.deque()
		q += [root]
		while q:
			s = len(q)
			sum_ = 0
			for i in range(s):
				node = q.popleft()
				sum_ += node.val
				if node.left:
					q += [node.left]
				if node.right:
					q += [node.right]

			res += [sum_ / s]

		return res

