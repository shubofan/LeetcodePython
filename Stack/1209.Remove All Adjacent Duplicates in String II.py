class Solution:
	def removeDuplicates(self, s: str, k: int) -> str:
		stack = []
		for v in s:
			if stack and stack[-1][0] == v:
				stack += [(v, stack[-1][1] + 1)]
			else:
				stack += [(v, 1)]
			if stack and stack[-1][1] == k:
				m = k
				while m > 0:
					stack.pop()
					m -= 1
		return ''.join([t[0] for t in stack])
