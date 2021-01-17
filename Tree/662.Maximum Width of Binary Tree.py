from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        dq = deque()
        dq.append((root, 1))

        while dq:

            l, r = 0, len(dq) - 1
            for i in range(len(dq)):
                cur, pos = dq.popleft()
                # get position of leftmost treeNode in current level
                if i == 0:
                    l = pos
                # get position of rightmost treeNode in current level
                if i == r:
                    r = pos
                if cur.left:
                    dq.append((cur.left, pos * 2))
                if cur.right:
                    dq.append((cur.right, pos * 2 + 1))
            res = max(res, r - l + 1)
        return res
