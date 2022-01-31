# TIME COMPLEXITY
# O(n)
#
# SPACE COMPLEXITY
# O(n) [ For stack ]
class Solution:
	# 1.Identify all indexes that should be removed.
	# 2.Build a new string without removed indexes.
	def minRemoveToMakeValid(self, s: str) -> str:
		# store index of parentheses to be removed
		stack = []
		indexes_to_remove = set()
		for idx, v in enumerate(s):
			if v == '(':
				stack += [idx]
			elif v == ')':
				if not stack:
					indexes_to_remove.add(idx)
				else:
					stack.pop()

		indexes_to_remove = indexes_to_remove.union(set(stack))  # remove remaining opening-parenthesis

		string_builder = []
		for i, v in enumerate(s):
			if i not in indexes_to_remove: # idx not in indexes_to_remove
				string_builder += [v]
		return ''.join(string_builder)