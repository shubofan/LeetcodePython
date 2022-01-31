from typing import List


class Solution:
	# time O(N), space O(N)
	def partitionLabels(self, s: str) -> List[int]:
		right_most = {}
		res = []
		for i, cha in enumerate(s):
			right_most[cha] = i
		l, r = 0, 0  # l -> begin of one partition, r -> end of one partition
		for i in range(len(s)):
			r = max(r, right_most[s[i]])
			if r == i:
				res += [r - l + 1]
				l = i + 1

		return res
