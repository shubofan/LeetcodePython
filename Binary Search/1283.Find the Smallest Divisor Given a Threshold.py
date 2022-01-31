class Solution:
	def smallestDivisor(self, nums: List[int], threshold: int) -> int:

		# get total sum for each divisor
		def getSum(nums, divisor):
			res = 0
			for num in nums:
				res += math.ceil(num / divisor)
			return res

		# the range of the divisor [1: max(nums)]
		l, r = 1, max(nums)

		while l < r:
			mid = (l + r) // 2

			# if mid is the divisor, change range to [mid+1:r]
			if getSum(nums, mid) > threshold:
				l = mid + 1
			else:
				# getSum(nums, mid) <= threshold: mid is a possible divisor
				r = mid
		return l