# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time O(N), where N is the number of nodes in the given tree.  BFS, DFS traverse each node
# Space O(N)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        stack = [root]
        root.pre = None
        res = []
        if k == 0:
            return [target.val]
        # A dfs, connect each node to its parent
        while stack:
            top = stack.pop()

            if top.left:
                top.left.pre = top
                stack += [top.left]
            if top.right:
                top.right.pre = top
                stack += [top.right]

        q = collections.deque()
        q += [target]

        seen = set()
        seen.add(target)
        # BFS to get the nodes with distance of K
        while q:
            size = len(q)
            while size > 0:
                top = q.popleft()
                # print(top.val)
                if top.left and top.left not in seen:
                    seen.add(top.left)
                    q += [top.left]
                if top.right and top.right not in seen:
                    seen.add(top.right)
                    q += [top.right]
                if top.pre and top.pre not in seen:
                    seen.add(top.pre)
                    q += [top.pre]
                size -= 1
            k -= 1

            if k == 0:
                break

        for node in q:
            res += [node.val]
        return res