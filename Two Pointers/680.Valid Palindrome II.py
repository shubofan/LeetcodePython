class Solution:
	def validPalindrome(self, s: str) -> bool:
		l, r = 0, len(s) - 1

		while l < r:
			if s[l] == s[r]:
				l += 1
				r -= 1

			else:
				# skip l
				candidate1 = s[l + 1:r + 1]

				# skip r
				candidate2 = s[l:r]

				if candidate1 != candidate1[::-1] and candidate2 != candidate2[::-1]:
					return False
				else:
					return True

		return True