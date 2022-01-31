# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.m = val

class Solution:


# def goodNodes(self, root: TreeNode) -> int:
#         # max value from root until current node
#         root.max_ = root.val
#         res = 0
#         stack = [root]
#         while stack:
#             top = stack.pop()
#             if top.max_ == top.val:
#                 res += 1

#             if top.left:
#                 top.left.max_ = max(top.max_, top.left.val)
#                 stack += [top.left]

#             if top.right:
#                 top.right.max_ = max(top.max_, top.right.val)
#                 stack += [top.right]
#         return res

def goodNodes(self, root: TreeNode) -> int:
	self.res = 0

	def dfs(root, max_):
		if not root:
			return
		if root.val >= max_:
			self.res += 1
		if root.left:
			dfs(root.left, max(max_, root.val))
		if root.right:
			dfs(root.right, max(max_, root.val))

	dfs(root, -float('inf'))
	return self.res