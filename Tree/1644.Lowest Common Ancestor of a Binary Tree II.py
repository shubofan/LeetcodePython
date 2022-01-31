"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

# 3 PASS
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # check if node in the tree
        def dfs(root, target):
            if not root:
                return None
            if root == target:
                return root
            l, r = dfs(root.left, target), dfs(root.right, target)

            return l or r


        def LCA(root, A, B):
            if not root or A == root or B == root:
                return root
            l = LCA(root.left, A, B)
            r = LCA(root.right, A, B)

            if l and r:
                return root
            elif l:
                return l
            else:
                return r
        # if A or B not in the tree, return None directly
        if not dfs(root, A) or not dfs(root, B):
            return None
        return LCA(root, A, B)

# 1 PASS
class Solution:
	"""
	@param: root: The root of the binary tree.
	@param: A: A TreeNode
	@param: B: A TreeNode
	@return: Return the LCA of the two nodes.
	"""

	def lowestCommonAncestor3(self, root, A, B):
		self.count = 0

		# post order traverse to make sure all node get visited
		def LCA(root, A, B):
			if not root:
				return root
			l = LCA(root.left, A, B)
			r = LCA(root.right, A, B)

			if root == A or root == B:
				self.count += 1
				return root

			if l and r:
				return root
			elif l:
				return l
			else:
				return r

		lca = LCA(root, A, B)
		if self.count == 2:
			return lca
		return None