class Solution:
	"""
	@param: nums: a sorted integer array
	@param: lower: An integer
	@param: upper: An integer
	@return: a list of its missing ranges

	Input:

	nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99

	Output:

	["2", "4->49", "51->74", "76->99"]

	Explanation:

	in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]
	"""

	def findMissingRanges(self, nums, lower, upper):
		# only Need this if the given array contains duplicate
		# nums = list(set(nums))
		# nums.sort()

		n = len(nums)
		res = []

		if n == 0:
			if lower != upper:
				return [str(lower) + '->' + str(upper)]
			else:
				return [str(lower)]

		if nums[0] > lower:
			if lower == nums[0] - 1:
				res += [str(lower)]
			else:
				res += [str(lower) + '->' + str(nums[0] - 1)]

		for i in range(n - 1):
			if nums[i + 1] - nums[i] == 1:
				continue
			elif nums[i + 1] - nums[i] == 2:
				res += [str(nums[i] + 1)]
			else:
				res += [str(nums[i] + 1) + '->' + str(nums[i + 1] - 1)]

		if nums[-1] < upper:
			if nums[-1] + 1 == upper:
				res += [str(upper)]
			else:
				res += [str(nums[-1] + 1) + '->' + str(upper)]

		return res