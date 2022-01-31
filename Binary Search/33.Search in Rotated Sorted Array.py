class Solution:
	def search(self, nums: List[int], target: int) -> int:
		n = len(nums)

		l, r = 0, n - 1

		# found the pivot
		while l < r:
			mid = (l + r) // 2
			if nums[mid] >= nums[r]:
				l = mid + 1
			else:
				r = mid

		pivot = l

		# search left part [0:pivot-1]
		l, r = 0, pivot - 1

		while l < r:
			mid = (l + r) // 2
			if nums[mid] < target:
				l = mid + 1
			else:
				r = mid
		if nums[l] == target:
			return l

		# search right part [pivot:n-1]
		l, r = pivot, n - 1

		while l < r:
			mid = (l + r) // 2
			if nums[mid] < target:
				l = mid + 1
			else:
				r = mid
		if nums[l] == target:
			return l
		else:
			return -1