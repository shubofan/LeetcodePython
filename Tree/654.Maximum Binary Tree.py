# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: helper will be call N times, for each call take O(1), so total O(N)
# Space: O(N), depth of stack will be O(N) when the nums is ordered
class Solution:
	def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
		# dic <value, index>
		d = {}

		for i, num in enumerate(nums):
			d[num] = i

		def helper(nums, l, r):
			if l == r:
				return None

			max_ = max(nums[l:r])
			idx = d[max_]

			node = TreeNode(max_)
			node.left = helper(nums, l, idx)
			node.right = helper(nums, idx + 1, r)
			return node

		return helper(nums, 0, len(nums))