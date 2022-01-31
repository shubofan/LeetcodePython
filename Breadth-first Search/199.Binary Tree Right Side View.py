# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        q = collections.deque()
        q += [root]
        while q:
            size = len(q)
            while size > 0:
                node = q.popleft()
                if size == 1:
                    res += [node.val]
                if node.left:
                    q += [node.left]
                if node.right:
                    q += [node.right]
                size -= 1
        return res