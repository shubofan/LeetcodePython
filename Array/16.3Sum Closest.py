from typing import Set


class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)
		diff = float('inf')

		for i in range(n - 2):
			l = i + 1
			r = n - 1
			while l < r:
				sum_ = nums[i] + nums[l] + nums[r]
				if abs(target - sum_) < abs(diff):
					diff = target - sum_
				if sum_ == target:
					return target
				elif sum_ - target < 0:
					l += 1
				elif sum_ - target > 0:
					r -= 1
		return target - diff

