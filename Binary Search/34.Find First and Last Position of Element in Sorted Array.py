class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		res = [-1, -1]
		if not nums:
			return res

		n = len(nums)
		l, r = 0, n - 1
		# find left
		while l < r:
			mid = (l + r) // 2
			if nums[mid] < target:
				l = mid + 1
			else:
				r = mid
		if nums[l] == target:
			res[0] = l

		l, r = 0, n - 1
		# find right
		while l < r:
			mid = (l + r + 1) // 2
			if nums[mid] <= target:
				l = mid
			else:
				r = mid - 1
		if nums[l] == target:
			res[1] = l
		return res