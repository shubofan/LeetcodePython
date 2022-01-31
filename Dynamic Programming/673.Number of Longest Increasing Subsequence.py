class Solution:
	def findNumberOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0
		n = len(nums)
		# dp[i] max length of increasing sub-sequences up to index i
		dp = [1] * n
		# max count of the longest increasing sub-sequences up to index i
		count = [1] * n

		for i in range(1, n):
			for j in range(i): # [0:i-1]
				if nums[i] > nums[j]:
					if dp[j] + 1 > dp[i]: # max length get updated
						dp[i] = dp[j] + 1
						count[i] = count[j]
					elif dp[j] + 1 == dp[i]: # max length to
						count[i] += count[j]

		max_lenth = max(dp)
		res = 0
		for i in range(n):
			if dp[i] == max_lenth:
				res += count[i]
		return res