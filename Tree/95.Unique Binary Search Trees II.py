# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1, n)

    def helper(self, l: int, r: int) -> List[TreeNode]:
        lst = []
        if l > r:
            lst += [None]
            return lst
        if l == r:
            lst += [TreeNode(l)]
            return lst
        # try to use i as root
        for i in range(l, r + 1):
            # get all left subtrees
            left_trees = self.helper(l, i - 1)
            # get all right subtrees
            right_trees = self.helper(i + 1, r)

            # merge left subtree and right subtree
            for ltree in left_trees:
                for rtree in right_trees:
                    root = TreeNode(i)
                    root.left = ltree
                    root.right = rtree
                    lst += [root]
        return lst


