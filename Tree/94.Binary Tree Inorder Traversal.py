# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		res = []
		if not root:
			return res

		stack = []
		cur = root
		while stack or cur:
			if cur:
				stack += [cur]
				cur = cur.left
			else:
				cur = stack.pop()
				res += [cur.val]
				cur = cur.right
		return res

