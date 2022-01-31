class Solution:
	def isMonotonic(self, nums: List[int]) -> bool:
		n = len(nums)
		if n <= 1:
			return True

		incr = False # increasing
		decr = False # decreasing

		for i in range(1, n):
			if nums[i] > nums[i - 1]:
				incr = True
			if nums[i] < nums[i - 1]:
				decr = True

		# if incr and decr: # not Monotonic
		#     return False
		return False if incr and decr else True