# Time: O(n), Space O(1)
'''
max_open counts the maximum open parenthesis, which means the maximum number of unbalanced '(' that COULD be paired.
min_open counts the minimum open parenthesis, which means the number of unbalanced '(' that MUST be paired.
'''


class Solution:
	def checkValidString(self, s: str) -> bool:
		max_open, min_open = 0, 0

		for i in s:
			if i == '(':
				max_open += 1
				min_open += 1
			if i == ')':
				max_open -= 1
				min_open -= 1

			if i == '*':
				max_open += 1
				min_open -= 1

			if max_open < 0:
				return False
			min_open = max(min_open,0)  # It's invalid if open parentheses count < 0 that's why min_open can't be negative. example: (** min_open cannot be negative, so mid * will be empty string

		return min_open == 0