from collections import Counter
import heapq


class Solution:
	def frequencySort(self, s: str) -> str:
		cnt = Counter(s)

		heap = []
		for c, fre in cnt.items():
			heapq.heappush(heap, (-fre, c))

		res = []
		while heap:
			fre, c = heapq.heappop(heap)
			res += c * (-fre)
		return ''.join(res)

# # bucket sort
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         n = len(s)
#         # idx is frequency, each element is another list if char List<List<Char>>
#         buckets = [None] * (n + 1)

#         cnt = Counter(s)

#         for c, fre in cnt.items():

#             if not buckets[fre]:
#                 buckets[fre] = []
#             buckets[fre] += [c]

#         res = []

#         for idx, lst in enumerate(buckets):
#             if lst:
#                 for i in lst:
#                     res.extend(i * idx)

#         return  ''.join(res[::-1])
