class Solution:
	def longestValidParentheses(self, s: str) -> int:
		res = 0
		stack = []
		# After the scan is done, the stack will only
		# contain the indices of characters which cannot be matched. Then
		# let's use the opposite side - substring between adjacent indices
		# should be valid parentheses.
		for idx, c in enumerate(s):
			if c == '(':
				stack += [idx]
			if c == ')':
				if not stack:
					stack += [idx]
				elif s[stack[-1]] == '(':
					stack.pop()
					if not stack:
						res = max(res, idx + 1)
					else:
						res = max(res, idx - stack[-1])
				else:
					stack += [idx]
		return res
