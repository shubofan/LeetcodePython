import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        fre = set()

        for key, v in cnt.items():
            heapq.heappush(heap, (v, key))
            if v not in fre:
                fre.add(v)
            if len(fre) > k:
                to_be_pop = heap[0][0]
                while to_be_pop == heap[0][0]:
                    heapq.heappop(heap)

                fre.remove(to_be_pop)

        return [word[1] for word in sorted(heap, key=lambda x: (-x[0], x[1]))][:k]
