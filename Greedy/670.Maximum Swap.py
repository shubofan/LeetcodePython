class Solution:
	# O(N)
	def maximumSwap(self, num: int) -> int:
		s = str(num)
		lst = list(s)
		n = len(lst)
		if len(s) == 1:
			return num

		# O(n)
		dic = {}  # <number, last index of this number in lst>
		for i, v in enumerate(lst):
			dic[int(v)] = i

		# O(n) * 9 = O(n)
		for i in range(n):
			val = int(lst[i])
			for large_v in range(9, val, -1):  # find largest number after position i
				if large_v in dic and dic[large_v] > i:
					lst[i], lst[dic[large_v]] = lst[dic[large_v]], lst[i]
					return int(''.join(lst))
		return num