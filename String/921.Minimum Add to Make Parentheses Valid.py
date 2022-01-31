class Solution:
	def minAddToMakeValid(self, s: str) -> int:
		remaining_right = 0
		stack = []
		for i in s:
			if i == '(':
				stack += [i]
			if i == ')':
				if stack:
					stack.pop()
				else:
					remaining_right += 1

		# len(stack) = remaining left
		return remaining_right + len(stack)