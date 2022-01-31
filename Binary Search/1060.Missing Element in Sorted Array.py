# http://leetcode.libaoj.in/missing-element-in-sorted-array.html
from typing import List


class Solution:
	def missingElement(self, nums: List[int], k: int) -> int:
		def totalMissingUntilIdx(nums, idx):  # number of missing elements until nums[idx]
			return nums[idx] - nums[0] + idx

		n = len(nums)
		# If kth missing number is larger than
		# the last element of the array
		if totalMissingUntilIdx(n - 1) < k:
			return nums[n - 1] + (k - totalMissingUntilIdx(n - 1))

		l , r = 0, n -1
		while l < r:
			mid = (l + r) //2
			if totalMissingUntilIdx(mid) < k:
				l = mid + 1
			else:
				r = mid

		# kth missing number is greater than nums[left - 1]
		# and less than nums[left]
		return nums[l - 1] + k - totalMissingUntilIdx(l - 1)
