"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
	"""
	@param: root: The root of the tree
	@param: A: node in the tree
	@param: B: node in the tree
	@return: The lowest common ancestor of A and B
	"""

	# def lowestCommonAncestorII(self, root, A, B):
	#     s = set()

	#     while A:
	#         s.add(A)
	#         A = A.parent

	#     while B:
	#         if B in s:
	#             return B
	#         else:
	#             B = B.parent

	'''
	p1, p2分别从A，B出发， 向root方向遍历。 p1达到root之后， 从B开始重新向root遍历。p2达到root之后， 从A开始重新向root遍历。
	p1和p2在第二次遍历时，一定会在第一个intersection（i.e LCA）相遇。 时间复杂度O(h)，h是数的最大高度。


	'''
	def lowestCommonAncestorII(self, root, A, B):
		if A == B:
			return A

		p, q = A, B

		while p != q:
			p = p.parent
			q = q.parent

			if not p:
				p = B
			elif not q:
				q = A

		return p

