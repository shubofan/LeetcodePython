class Solution:
	def mySqrt(self, x: int) -> int:

		l, r = 0, x
		while l < r:
			mid = (l + r + 1) // 2

			if mid ** 2 <= x:
				l = mid

			else:
				r = mid - 1

		return l