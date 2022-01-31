import collections
from collections import Counter


class Solution:
	# O(C⋅∣s∣+∣t∣), C is the size of alphabet
	def minWindow(self, s: str, t: str) -> str:

		# O(|t|)
		self.cnt = Counter(t)
		res = ''
		l, r = 0, 0
		s_cnt = collections.defaultdict(int)
		n = len(s)

		while l < n and r < n:
			s_cnt[s[r]] += 1
			while self.check(s_cnt) and l <= r:
				if not res: # s[l:r+1] is a good candidate
					res = s[l:r + 1]
				elif len(s[l:r + 1]) < len(res):
					res = s[l:r + 1]
				s_cnt[s[l]] -= 1
				l += 1
			r += 1

		return res

	def check(self, s_cnt):
		# O(1) since the number of key is fixed.
		for c, fre in self.cnt.items():
			if c not in s_cnt:
				return False
			elif fre > s_cnt[c]:
				return False
		return True