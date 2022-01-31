class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		# 数列中除了我们目标数，其它都出现了三次。将数列中每个数用二进制表示，那在各位上出现的次数至少是3、或3的倍数，从这个思路出发，
		# 我们用ones、twos分别统计各位上出现1次、2次的个数。
		ones, twos = 0, 0

		for num in nums:
			# (ones ^ A[i])两个数异或是把两个数各自位上的1、0相减的绝对值。
			# # & ~twos  ---- 是为了出现3次后清0
			ones = (ones ^ num) & ~(twos)

			twos = (twos ^ num) & ~(ones)

		return ones