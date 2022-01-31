class Solution:
	def countPalindromicSubsequence(self, s: str) -> int:
		d = collections.defaultdict(list)
		for i, c in enumerate(s):
			d[c] += [i]

		res = 0

		for char, lst in d.items():
			if len(lst) < 2:
				continue

			first_pos, last_pos = lst[0], lst[-1]

			# PalindromicSubsequence -> char,middle,char

			# set(s[first_pos+1:last_pos]) all the possible middle elements
			res += len(set(s[first_pos + 1:last_pos]))

		return res