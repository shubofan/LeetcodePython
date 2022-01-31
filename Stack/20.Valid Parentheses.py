class Solution:
	def isValid(self, s: str) -> bool:
		stack = []

		for i in s:
			if stack:
				if i == ']' and stack[-1] == '[':
					stack.pop()

				elif i == ')' and stack[-1] == '(':
					stack.pop()

				elif i == '}' and stack[-1] == '{':
					stack.pop()
				else:
					stack += [i]
			else:
				stack += [i]

		return not stack