class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		# Binary search
		#         n = len(nums)
		#         prefix_sum = [0] * (n + 1)
		#         res = n + 1
		#         for i in range(n):
		#             prefix_sum[i + 1] = nums[i] + prefix_sum[i]

		#         for i in range(1, n + 1):
		#             l , r = i, n

		#             to_find = prefix_sum[i - 1] + target

		#             while l < r:
		#                 mid = (l + r) // 2
		#                 if prefix_sum[mid] < to_find:
		#                     l = mid + 1
		#                 else:
		#                     r = mid

		#             if l <= n and prefix_sum[l] >= to_find:

		#                 res = min(res, l - i + 1)

		#         return 0 if res == n + 1 else res

		# sliding window
		n = len(nums)
		res = n + 1
		l, r = 0, 0
		s = 0
		while r < n:
			s += nums[r]
			while s >= target and l <= r:  # sum ([l, r]) >= target
				res = min(res, r - l + 1)
				s -= nums[l]
				l += 1
			r += 1
		return 0 if res == n + 1 else res
