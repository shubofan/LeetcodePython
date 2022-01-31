class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		xor = 0
		#  先对所有数字进行一次异或，得到两个出现一次的数字的异或值。

		# 在异或结果中找到最后为 1 的位。

		# 根据这一位对所有的数字进行分组。

		# 在每个组内进行异或操作，得到两个数字。

		for num in nums:
			xor ^= num

		last_one = 1

		while last_one & xor == 0:
			last_one <<= 1
		a, b = 0, 0
		for num in nums:

			if last_one & num == 0:
				a ^= num
			else:
				b ^= num
		return [a, b]