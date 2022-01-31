# Sort + DP + Longest Increasing Subsequence

# Time: O(n log n)
from typing import List


class Solution:
	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
		n = len(envelopes)

		# if sorted x[1] ascendingly, like [(1,1),(1,2),(1,3),(1,4)]  - > [1,2,3,4] , LIS = 4 which is wrong

		# if sorted x[1] descendingly, like [(1,4),(1,3),(1,2),(1,1)]  - > [4,3,2,1] , LIS = 1 which is right!
		envelopes.sort(key=lambda x: (x[0], -x[1]))

		lis = [envelopes[0][1]]  # the longest increase sequence

		for i in range(1, n):
			envelope = envelopes[i]

			if envelope[1] > lis[-1]:  # only possible when envelope[0] > lis[-1] like [1,3], [2, 4]
				lis += [envelope[1]]
			else:
				l, r = 0, len(lis) - 1
				while l < r:
					mid = (l + r) // 2
					if lis[mid] < envelope[1]:
						l = mid + 1
					else:
						r = mid

				lis[l] = envelope[1]

		return len(lis)
