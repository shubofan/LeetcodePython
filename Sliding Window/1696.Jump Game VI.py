# Deque, Mono-queue + DP

# Time complexity: O(n)
# Space complexity: O(n+k) -> O(n)
import collections


class Solution:
	def maxResult(self, nums, k):
		deq, n = collections.deque([0]), len(nums)
		dp = [0] * n  # dp[i] max score got until i
		dp[0] = nums[0]
		for i in range(1, n):
			# index increase in deque
			while deq and deq[0] < i - k:
				deq.popleft()

			# dp[deq[0]] is the maximum dp value in range.
			dp[i] += nums[i] + dp[deq[0]]

			# value decrease in mono queue
			while deq and dp[i] >= dp[deq[-1]]:
				deq.pop()
			deq.append(i)

		return dp[-1]

