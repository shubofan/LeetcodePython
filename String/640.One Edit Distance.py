class Solution:
	"""
	Time complexity : (N) in the worst case when string lengths are close enough abs(ns - nt) <= 1 ,
	where N is a number of characters in the longest string

	Space complexity : O(1)

	"""

	def isOneEditDistance(self, s, t):
		if len(s) > len(t):
			return self.isOneEditDistance(t, s)

		# ls <= lt
		ls, lt = len(s), len(t)

		if lt - ls > 1:
			return False

		i = 0

		while i < ls:
			if s[i] != t[i]:
				# two string has same length
				if ls == lt:
					return s[i + 1:] == t[i + 1:]
				# two string has different length, lt - ls == 1, remove t[i] from t
				else:
					return s[i:] == t[i + 1:]
			i += 1

		# no difference in first ls, so check if t has one more character
		return ls + 1 == lt