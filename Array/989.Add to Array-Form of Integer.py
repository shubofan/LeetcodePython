class Solution:
	#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
	#         num = map(lambda x:str(x) , num)
	#         s = ''.join(num)
	#         sum_ = int(s) + k

	# return [int(x) for x in list(str(sum_))]

	def addToArrayForm(self, num: List[int], k: int) -> List[int]:
		n = len(num)
		carry = 0
		i = n - 1

		# print(i)
		while i >= 0 or k > 0:
			op = k % 10
			k //= 10
			if i >= 0:
				sum_ = num[i] + op + carry
				num[i] = sum_ % 10
				carry = sum_ // 10
				i -= 1
			else:
				sum_ = (op + carry) % 10
				carry = (op + carry) // 10

				num.insert(0, sum_)

		if carry:
			return [1] + num
		return num
