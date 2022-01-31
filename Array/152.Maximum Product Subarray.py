class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		if not nums:
			return 0
		cur_min, cur_max, res = nums[0], nums[0], nums[0]

		# cur_max: max product ending with nums[i]
		# cur_min: min product ending with nums[i]
		# so cur_max[i] = max(cur_min[i -1] * nums[i], cur_max*nums[i - 1], nums[i]) and cur_min = min(cur_min[i -1] * nums[i], cur_max*nums[i - 1])
		for i in range(1, len(nums)):
			pre_max = cur_max
			pre_min = cur_min
			cur_max = max(pre_min * nums[i], pre_max * nums[i], nums[i])
			cur_min = min(pre_min * nums[i], pre_max * nums[i], nums[i])
			res = max(res, cur_max)
		return res