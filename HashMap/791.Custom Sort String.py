class Solution:
	def customSortString(self, order: str, s: str) -> str:
		cnt = collections.Counter(s)

		res = ''

		for c in order:
			if c in cnt:
				res += cnt[c] * c
				cnt.pop(c)

		for char, fre in cnt.items():
			res += char * fre

		return res