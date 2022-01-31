# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #     def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #         res = []
    #         stack = []
    #         stack = [(root, str(root.val)+ '->')]
    #         while stack:
    #             node, path = stack.pop()
    #             # print(path)
    #             if not node.left and not node.right:
    #                 res += [path[:len(path) - 2]]
    #             else:
    #                 if node.left:
    #                     stack += [(node.left, path + str(node.left.val) + '->')]
    #                 if node.right:
    #                     stack += [(node.right, path + str(node.right.val) + '->')]

    #         return res

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []

        def helper(root, path):
            # leaf
            if not root.left and not root.right:
                self.res += [path]
                return
            if root.left:
                helper(root.left, path + '->' + str(root.left.val))
            if root.right:
                helper(root.right, path + '->' + str(root.right.val))

        helper(root, str(root.val))
        return self.res