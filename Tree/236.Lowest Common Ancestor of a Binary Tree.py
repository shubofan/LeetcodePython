# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #         stack = []

    #         if not root:
    #             return root
    #         dic = {root:None}
    #         stack += [root]

    #         while stack:
    #             parent = stack.pop()
    #             if parent.left:
    #                 dic[parent.left] = parent
    #                 stack += [parent.left]
    #             if parent.right:
    #                 dic[parent.right] = parent
    #                 stack += [parent.right]

    #         ancestor = set()

    #         while p:
    #             ancestor.add(p)
    #             p = dic[p]

    #         while q:
    #             if q in ancestor:
    #                 return q
    #             q = dic[q]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif not left:
            return right
        elif not right:
            return left