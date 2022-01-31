# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections


# Time: O(N) N is the number if node in the root. since we performed 2 BFS
# Space: O(R*C) where R is size of the row of matrix and C is the size of columns for matrix
from typing import Optional, List

class Solution:
  def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        q = collections.deque()
        q += [root]
        height = 0

        # get height
        while q:
            size = len(q)
            while size > 0:
                cur = q.popleft()
                if cur.left:
                    q += [cur.left]
                if cur.right:
                    q += [cur.right]
                size -= 1

            height += 1

        height -= 1 # get actual height start from 0, height = 0 means just have a root node
        m = height + 1
        n = 2 ** m - 1

        res = [[''] * n for _ in range(m)]

        q = collections.deque()
        q += [root]
        root.x = 0
        root.y = (n - 1) // 2

        while q:
            cur = q.popleft()
            row = cur.x
            col = cur.y
            res[row][col] = str(cur.val)
            if cur.left:
                q += [cur.left]
                cur.left.x = row + 1
                cur.left.y = col - 2 ** (height - row - 1)

            if cur.right:
                q += [cur.right]
                cur.right.x = row + 1
                cur.right.y = col + 2 ** (height - row - 1)

        return res