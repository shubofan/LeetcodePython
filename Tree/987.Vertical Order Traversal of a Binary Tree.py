from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        pos = {}
        root.row = 0
        root.col = 0
        q = deque()
        q += [root]
        while q:
            top = q.popleft()
            x, y = top.row, top.col
            if y not in pos:
                pos[y] = {}
            if x not in pos[y]:
                pos[y][x] = []
            pos[y][x] += [top.val]
            if top.left:
                top.left.col = top.col - 1
                top.left.row = top.row + 1
                q += [top.left]
            if top.right:
                top.right.col = top.col + 1
                top.right.row = top.row + 1
                q += [top.right]

        cols = sorted(pos.keys())
        for col in cols:
            tem = []
            for row in pos[col]:
                # same position, sort by value 
                tem.extend(sorted(pos[col][row]))
            res.append(tem[::])
        return res