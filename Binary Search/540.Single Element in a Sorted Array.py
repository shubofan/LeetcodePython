from typing import List


class Solution:
	def singleNonDuplicate(self, nums: List[int]) -> int:
		n = len(nums)
		if n == 1:
			return nums[0]
		l, r = 0, n - 1
		while l < r:
			mid = (l + r) // 2
			if nums[mid] == nums[mid - 1]:
				if mid % 2 == 0:  # like 12233
					r = mid - 2
				else:
					l = mid + 1  # 223
			elif nums[mid] == nums[mid + 1]:
				if mid % 2 == 0:  # like 11223
					l = mid + 2
				else:
					r = mid - 1  # 122
			else:  # nums[mid] is the element appears only onetime
				return nums[mid]
		return nums[l]