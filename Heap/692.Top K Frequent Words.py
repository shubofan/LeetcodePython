import heapq
# Time (nlogk)
# Space (n)
from collections import Counter


class WordWithFreq:
	def __init__(self, word, freq):
		self.freq = freq
		self.word = word

	def __lt__(self, other):
		# if freq same, sort by alphabetic order reversely
		if self.freq == other.freq:
			return self.word > other.word
		return self.freq < other.freq


# heap top, fre is min, word  alphabetical is max, so pop order is [least_fre1, least_fre2_high_alphabetical, least_fre2_low_alphabetical]
# revered [least_fre2_low_alphabetical, least_fre2_high_alphabetical, least_fre1]
class Solution:
	def topKFrequent(self, words: List[str], k: int) -> List[str]:
		cnt = Counter(words)
		heap = []
		res = []
        # n * log(k)
		for word, fre in cnt.items():
			heapq.heappush(heap, (fre, WordWithFreq(word, fre)))
			# keep the size of heap <= k, so log(k)
			if len(heap) > k:
				heapq.heappop(heap)
		while heap:
			res += [heapq.heappop(heap)[1].word]
		return res[::-1]