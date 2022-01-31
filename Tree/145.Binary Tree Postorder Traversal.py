# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		res, stack = [], [root]
		if not root:
			return res

		while stack:
			top = stack.pop()
			res += [top.val]
			if top.left:
				stack += [top.left]
			if top.right:
				stack += [top.right]
		# add order is root - r - l, so reserve will be   l - r - root
		res.reverse()
		return res
