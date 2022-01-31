# O(N) traverse two strings
# O(1) two pointers
class Solution:
	# the relative order of L and R should be same in start and end
	def canTransform(self, start: str, end: str) -> bool:
		n = len(start)

		i, j = 0, 0

		# count X in start and end should be the same
		if start.count('X') != end.count('X'):
			return False

		while i < n or j < n:
			# Move to next L or R in start
			while i < n and start[i] == 'X':
				i += 1
			# Move to next L or R in end
			while j < n and end[j] == 'X':
				j += 1

			# if reach end, check if both i and j reached end
			if i == n or j == n:
				return i == j

			# relative order is not same
			if start[i] != end[j]:
				return False

			# i < j, since L cannot go to left, start[i]=L never go right to j, so return False. eg: XLX can NOT become to XXL
			if start[i] == 'L' and i < j:
				return False

			# i > j, since R cannot go to left, start[i]=R never go left to j, so return False eg: XRX can NOT become to RXX
			if start[i] == 'R' and i > j:
				return False

			i += 1
			j += 1

		return True