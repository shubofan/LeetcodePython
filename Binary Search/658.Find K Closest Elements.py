class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		n = len(arr)
		l, r = 0, n - 1

		while l < r:
			mid = (l + r) // 2
			if arr[mid] < x:
				l = mid + 1
			else:
				r = mid

		# find the Closest one
		pos = l
		l, r = max(0, pos - k), min(pos + k, n - 1)

		# shrink from [l:r], approximate 2k elements

		while r - l + 1 > k:
			if x - arr[l] <= arr[r] - x:
				r -= 1
			else:
				l += 1
		return arr[l:r + 1]