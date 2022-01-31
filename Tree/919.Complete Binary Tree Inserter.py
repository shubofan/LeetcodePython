# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

	def __init__(self, root: Optional[TreeNode]):
		self.tree = []
		q = collections.deque()
		q += [root]
		while q:
			node = q.popleft()
			self.tree += [node]
			if node.left:
				q += [node.left]
			if node.right:
				q += [node.right]

	# O(1)
	#  Node tree[i] has left child tree[2 * i + 1] and tree[2 * i + 2]
	def insert(self, val: int) -> int:

		N = len(self.tree)
		self.tree.append(TreeNode(val))
		if N % 2:
			self.tree[(N - 1) // 2].left = self.tree[-1]
		else:
			self.tree[(N - 1) // 2].right = self.tree[-1]
		return self.tree[(N - 1) // 2].val

	def get_root(self) -> Optional[TreeNode]:
		return self.tree[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()