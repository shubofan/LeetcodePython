class Solution:
	"""
	Time Complexity: O(QK), where Q is the length of words (at least 1), and K is the maximum length of a word.

	Space Complexity: O(K)

	"""

	def expressiveWords(self, s: str, words: List[str]) -> int:
		res = 0
		for word in words:
			if self.isStretchy(s, word):
				res += 1

		return res

	def isStretchy(self, s, word):
		# get length of repeats letters in s start from i
		def getRepeat(s, i):
			j = i
			while j < len(s):
				if s[i] == s[j]:
					j += 1
				else:
					break
			return j - i

		i, j = 0, 0
		while i < len(s) and j < len(word):
			if s[i] != word[j]:
				return False

			l1, l2 = getRepeat(s, i), getRepeat(word, j)

			# repeats < 3, l1 must == l2, otherwise like aa, a, return fasle
			# repeats >= 3, however, l1 < l2, like aaa, aaaa, return false
			if l1 < 3 and l1 != l2 or l1 >= 3 and l1 < l2:
				return False

			i += l1
			j += l2

		return i == len(s) and j == len(word)  # check if both two pointers reach the end of two strings

