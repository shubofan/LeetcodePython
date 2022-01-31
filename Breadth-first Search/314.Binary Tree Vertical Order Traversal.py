"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:
	"""
	@param root: the root of tree
	@return: the vertical order traversal
	"""

	def verticalOrder(self, root):
		res = []
		if not root:
			return res

		q = collections.deque()
		q += [(root, 0)]
		dic = collections.defaultdict(list)

		while q:
			top, pos = q.popleft()

			dic[pos] += [top.val]
			if top.left:
				q += [(top.left, pos - 1)]
			if top.right:
				q += [(top.right, pos + 1)]

		for k in sorted(dic.keys()):
			res += [dic[k]]
		return res