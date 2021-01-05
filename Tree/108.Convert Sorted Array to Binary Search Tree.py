# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums: List[int], start: int, end: int) -> TreeNode:
        mid = int((start + end) // 2)

        if mid < start or mid > end:
            return None

        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid - 1)
        root.right = self.dfs(nums, mid + 1, end)
        return root
