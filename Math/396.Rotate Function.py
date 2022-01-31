class Solution:
	def maxRotateFunction(self, nums: List[int]) -> int:
		res = 0
		n = len(nums)

		fn = sum([idx * num for idx, num in enumerate(nums)])  # f0
		s = sum(nums)
		i = 1
		res = fn

		r = n - 1
		while i < n:
			fn = fn + s - n * nums[r]
			r -= 1
			i += 1
			res = max(res, fn)

		return res