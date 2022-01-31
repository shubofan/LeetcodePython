class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		if num == 1:
			return True

		l = 2
		r = num // 2

		while l < r:
			mid = (l + r) // 2
			if mid ** 2 < num:
				l = mid + 1
			else:
				r = mid

		return l ** 2 == num