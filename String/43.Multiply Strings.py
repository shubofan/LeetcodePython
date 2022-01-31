class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		if num1 == '0' or num2 == '0':
			return '0'
		if num1 == '1':
			return num2

		if num2 == '1':
			return num1

		l1, l2 = len(num1), len(num2)

		self.res = ''
		self.tem = ''
		n = 0  # append number of 0s each time
		# Time O(m) * (m + n) = O(m*n + m^2)
		# Space O(m+n)
		for i in range(l1 - 1, -1, -1):
			digit = num1[i]
			# O(n)
			self.tem = self.multiplyStrings(digit, num2)
			# O(m + n)
			self.res = self.addStrings(self.res, self.tem + n * '0')
			n += 1
		return self.res

	# nums1 will always be a digits
	# O(n)
	def multiplyStrings(self, num1: str, num2: str) -> str:
		i = len(num2) - 1
		carry = 0
		ans = []
		x = int(num1[0])
		while i >= 0 or carry != 0:
			y = int(num2[i]) if i >= 0 else 0
			result = x * y + carry
			ans.append(str(result % 10))
			carry = result // 10
			i -= 1

		return "".join(ans[::-1])

	# O(m + n)
	def addStrings(self, num1: str, num2: str) -> str:
		i, j = len(num1) - 1, len(num2) - 1
		carry = 0
		ans = []
		while i >= 0 or j >= 0 or carry != 0:
			x = int(num1[i]) if i >= 0 else 0
			y = int(num2[j]) if j >= 0 else 0
			result = x + y + carry
			ans.append(str(result % 10))
			carry = result // 10
			i -= 1
			j -= 1
		return "".join(ans[::-1])
