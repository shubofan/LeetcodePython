class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		l1, l2 = len(num1) - 1, len(num2) - 1
		res = []
		carry = 0
		while l1 >= 0 or l2 >= 0:
			op1 = 0
			if l1 >= 0:
				op1 = int(num1[l1])
			op2 = 0
			if l2 >= 0:
				op2 = int(num2[l2])
			s = carry + op1 + op2
			res += [s % 10]
			carry = s // 10
			l1 -= 1
			l2 -= 1
		if carry:
			res += [carry]
		return ''.join([str(x) for x in res[::-1]])

