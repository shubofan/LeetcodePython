class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		# Time: O(M + N), Space O (M+N)
		#         stack1 = []
		#         stack2 = []

		#         for i in s:
		#             if i == '#' and stack1:
		#                 stack1.pop()
		#             if i != '#':
		#                 stack1 += [i]

		#         for i in t:
		#             if i == '#' and stack2:
		#                 stack2.pop()
		#             if i != '#':
		#                 stack2 += [i]

		#         return stack1 == stack2

		# Time: O(M + N), Space O (1)
		def getStr(s):
			n = len(s)
			r = n - 1
			res = []
			count = 0  # backSpace count
			while r >= 0:
				if s[r] == '#':
					count += 1
				else:
					if count > 0:  # delete current char and decrement count of backspace
						count -= 1
					else:
						res += [s[r]]
				r -= 1
			return res

		return getStr(s) == getStr(t)