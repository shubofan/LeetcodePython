class Solution:
	def diStringMatch(self, s: str) -> List[int]:
		n = len(s)
		l, r = 0, n
		res = []
		i = 0

		while i < n:
			if s[i] == 'I':
				res += [l]
				l += 1
			else:
				res += [r]
				r -= 1
			i += 1

		return res + [l]  # last number l == r