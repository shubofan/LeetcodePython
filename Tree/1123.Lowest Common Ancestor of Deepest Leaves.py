# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
	def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
		def helper(root: TreeNode) -> (TreeNode, int):  # (LCA , max_depth)
			if not root:
				return (None, 0)
			l_node, l_depth = helper(root.left)
			r_node, r_depth = helper(root.right)
			if l_depth == r_depth:  # l and r have same depth, root is LCA
				return (root, l_depth + 1)
			if l_depth > r_depth:  # l_depth > r_depth, l_node is LCA
				return (l_node, l_depth + 1)
			if l_depth < r_depth:
				return (r_node, r_depth + 1)

		if not root:
			return root

		return helper(root)[0]

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # key is node, value is its parent
        m = {root: root}
        deepest_leaves = []
        deepest_level = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level > deepest_level:
                deepest_leaves = [node]
                deepest_level = level
            elif level == deepest_level:
                deepest_leaves += [node]
            if node.left:
                m[node.left] = node
                stack += [(node.left, level + 1)]
            if node.right:
                m[node.right] = node
                stack += [(node.right, level + 1)]

        # single leaf
        if len(deepest_leaves) == 1:
            return deepest_leaves[0]

        while True:
            parents = set()
            for idx, node in enumerate(deepest_leaves):
                parents.add(m[node])
                parent = m[node]
                deepest_leaves[idx] = parent
            # common parent for the all the children
            if len(parents) == 1:
                break

        return parents.pop()


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def get_max_height(root: TreeNode) -> int:
            if not root:
                return 0
            return 1 + max(get_max_height(root.left), get_max_height(root.right))

        if not root:
            return root

        l_height = get_max_height(root.left)
        r_height = get_max_height(root.right)

        if l_height == r_height:  # both left and right sub trees contain deepest leaves, so root if the LCA
            return root
        elif l_height > r_height:  # right sub tree does not contain deepest leaves
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)