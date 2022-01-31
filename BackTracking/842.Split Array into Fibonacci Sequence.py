#   时间复杂度：O(n)*(log⁡C)^2，其中 nnn 是字符串的长度，C 是题目规定的整数范围 2 ^31 -1。 对于前 222 个数，它们的位数不能超过 log⁡10C，那么枚举的空间为 O(log⁡C) ^ 2

# 在回溯的过程中，实际上真正进行「回溯」的只有前 2 个数，而从第 3 个数开始，整个斐波那契数列是可以被唯一确定的，整个回溯过程只起到验证（而不是枚举）的作用。

# 空间复杂度：O(n)，其中 n 是字符串的长度。除了返回值以外，空间复杂度主要取决于回溯过程中的递归调用层数，最大为 n
from typing import List

class Solution:
	def splitIntoFibonacci(self, num: str) -> List[int]:
		self.res = []
		self.helper(num, [])
		return self.res

	def helper(self, num, path):

		if not num:
			if len(path) >= 3:
				self.res = path

		if len(path) < 2:
			for i in range(1, len(num) + 1):
				# leading zero
				if len(num[:i]) > 1 and num[:i][0] == '0':
					continue
				self.helper(num[i:], path + [num[:i]])
		else:
			target = int(path[-1]) + int(path[-2])
			if target > 2 ** 31:
				return
			for i in range(1, len(num) + 1):
				if len(num[:i]) > 1 and num[:i][0] == '0':
					continue
				if int(num[:i]) > target:
					return
				if int(num[:i]) == target:
					self.helper(num[i:], path + [num[:i]])