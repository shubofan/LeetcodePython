# Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time and we have 2n-1 centers in total, the overall complexity is O(n^2)

# Space complexity : O(1)


class Solution:
	def longestPalindrome(self, s: str) -> str:
		def expand(s, l, r):
			while l >= 0 and r < len(s) and s[l] == s[r]:
				l -= 1
				r += 1
			return s[l + 1:r]

		res = ''
		for i in range(len(s)):
			l1 = expand(s, i, i)
			if len(l1) > len(res):
				res = l1
			if i + 1 < len(s):
				l2 = expand(s, i, i + 1)
				if len(l2) > len(res):
					res = l2

		return res