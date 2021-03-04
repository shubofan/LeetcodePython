from collections import deque


# Definition for a Node.
class Node:
    from typing import List

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            size = len(q)
            while size > 0:
                cur = q.popleft()
                level += [cur.val]
                for child in cur.children:
                    q.append(child)
                size -= 1
            res += [level]
        return res
