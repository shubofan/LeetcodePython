# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #     def kthSmallest(self, root: TreeNode, k: int) -> int:
    #         res = []
    #         stack = []
    #         cur = root
    #         while stack or cur:

    #             if cur:
    #                 stack += [cur]
    #                 cur = cur.left
    #             else:
    #                 cur = stack.pop()

    #                 res += [cur.val]

    #                 if len(res) == k:
    #                     return res[-1]
    #                 cur = cur.right

    #         return res[-1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.rebuild(root)
        return self.helper(root, k)

    def helper(self, root: TreeNode, k: int) -> int:
        left_count, right_count = 0, 0
        if root.left:
            left_count = root.left.val[1]
        if root.right:
            right_count = root.right.val[1]
        if k == left_count + 1:
            return root.val[0]
        if k > left_count:
            return self.helper(root.right, k - left_count - 1)
        else:
            return self.helper(root.left, k)

    # rebuild the entire tree, so that for each node, the val become a tuple like (val, total_count_of_its_subtree_with_itself)
    def rebuild(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_count = self.rebuild(root.left)
        right_count = self.rebuild(root.right)
        count = 1 + left_count + right_count
        root.val = (root.val, count)
        return count