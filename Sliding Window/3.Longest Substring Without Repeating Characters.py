class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		window = set()

		l, r = 0, 0
		n = len(s)
		res = 0
		while r < n:
			# window s[l:r+1]
			if s[r] not in window:
				window.add(s[r])
				res = max(res, r - l + 1)
				r += 1
			else:
				window.remove(s[l])
				l += 1

		return res