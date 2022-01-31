class Solution:
	def findShortestSubArray(self, nums: List[int]) -> int:
		n = len(nums)
		res = n
		degree = 0
		d = collections.defaultdict(list)

		for i, num in enumerate(nums):
			d[num] += [i]
			lst = d[num]
			if len(d[num]) > degree:
				degree = len(d[num])
				res = i - lst[0] + 1
			if len(d[num]) == degree:
				degree = len(d[num])
				res = min(res, lst[-1] - lst[0] + 1)

		return res