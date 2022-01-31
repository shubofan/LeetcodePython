# Time complexity: O(N), where N is a number of nodes. During preorder traversal, each node is visited once.

# Space complexity: up to O(N) to keep the hashmap of prefix sums, where N is a number of nodes.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
	def pathSum(self, root: TreeNode, targetSum: int) -> int:
		self.res = 0
		self.presum = collections.defaultdict(int)  # key is current sum and value if number of paths whose sum is =
		self.getSum(root, 0, targetSum)
		return self.res

	def getSum(self, root: TreeNode, curSum: int, targetSum: int) -> None:
		if not root:
			return 0
		curSum += root.val

		if curSum == targetSum:
			self.res += 1
		self.res += self.presum[curSum - targetSum]

		self.presum[curSum] += 1
		if root.left:
			self.getSum(root.left, curSum, targetSum)

		if root.right:
			self.getSum(root.right, curSum, targetSum)
		# remove the current sum from the hashmap
		# in order not to use it during
		# the parallel subtree processing
		self.presum[curSum] -= 1