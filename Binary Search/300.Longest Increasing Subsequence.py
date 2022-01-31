from typing import List


class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0

	# dp[i] represents the length of the longest increasing subsequence up to ith index only
	# dp = [0] * len(nums)
	# res = 0
	# for i in range(len(nums)):
	#     dp[i] = 1
	#     for j in range(i):
	#         if nums[j] < nums[i]:
	#             dp[i] = max(dp[j] + 1, dp[i])
	# return max(dp)

	# Binary search
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0
		# subsequence is the Longest Increasing Subsequence
		subsequence = []
		subsequence += [nums[0]]

		for num in nums:
			# if current nums is greater than the largest one in subsequence, append it directly
			if num > subsequence[-1]:
				subsequence += [num]
			else:
				# found the 1st element in seq which is greater than num, and replace it
				l, r = 0, len(subsequence) - 1
				while l < r:
					mid = int(l + (r - l) / 2)
					if num > subsequence[mid]:
						l = mid + 1
					elif num <= subsequence[mid]:
						r = mid
				subsequence[l] = num
		return len(subsequence)

