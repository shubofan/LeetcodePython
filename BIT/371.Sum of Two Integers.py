class Solution:
	def getSum(self, a: int, b: int) -> int:
		if a == 0:
			return b
		if b == 0:
			return a

		mask = 0xFFFFFFFF
		# After each operation we have an invisible & mask , where mask = 0xFFFFFFFF , i.e. bitmask of 32 1-bits.
		# keep just 32 bits of int

		# a is res
		# b is carry
		while b != 0:
			a, b = (a ^ b) & mask, ((a & b) << 1) & mask

		max_int = 0x7FFFFFFF  # 0111 FFFF FFFF FFFF = 2147483647
		return a if a < max_int else ~(a ^ mask)