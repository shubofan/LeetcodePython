class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		positive = (dividend < 0) == (divisor < 0)
		dividend, divisor = abs(dividend), abs(divisor)
		l, r = 0, dividend
		while l < r:
			mid = (l + r + 1) // 2
			if mid * divisor <= dividend:
				l = mid
			else:
				r = mid - 1

		if not positive:
			l = -l
		return min(max(-2147483648, l), 2147483647)
