class Solution:
	# palindromic centers is 2n−1
	# O(n * (2n - 1)) = O(n^2)
	def countSubstrings(self, s: str) -> int:
		n = len(s)
		res = 0
		for i in range(n):
			res += self.expand(s, i, i)
			res += self.expand(s, i, i + 1)
		return res

	def expand(self, s: str, l: int, r: int) -> int:
		count = 0
		while l >= 0 and r < len(s):
			if s[l] == s[r]:
				l -= 1
				r += 1
				count += 1
			else:
				break
		return count