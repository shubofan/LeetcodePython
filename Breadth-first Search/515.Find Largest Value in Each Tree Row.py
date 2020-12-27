# Definition for a binary tree node.
from collections import deque
import math
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        queue = deque()
        if not root:
            return res
        queue.append(root)
        while queue:
            level_size = len(queue)
            max_val = math.pow(-2, 32) * -1
            while level_size > 0:
                top = queue.popleft()
                max_val = max(max_val, top.val)
                level_size -= 1
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res += [max_val]
        return res
