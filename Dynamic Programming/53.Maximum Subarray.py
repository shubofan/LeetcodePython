class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		# dp[i] max sum of continuous array until nums[i]
		n = len(nums)
		dp = [0] * n
		dp[0] = nums[0]

		for i in range(1, n):
			dp[i] = max(0, dp[i - 1]) + nums[i]

		return max(dp)