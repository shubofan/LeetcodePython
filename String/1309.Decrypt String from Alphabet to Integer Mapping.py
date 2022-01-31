class Solution:
	def freqAlphabets(self, s: str) -> str:
		res = []
		n = len(s)
		r = n - 1
		while r >= 0:
			if s[r] == '#':
				res += [int(s[r - 2:r])]
				r -= 3
			else:
				res += [int(s[r:r + 1])]
				r -= 1

		res.reverse()

		res = [chr(i + 96) for i in res]
		return ''.join(res)