from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if not bank or end not in bank:
            return -1
        if start in bank:
            bank.remove(start)
        q = deque()
        q += [(start, 0)]
        replacements = ['A', 'C', 'G', 'T']

        while q:
            seq, level = q.popleft()

            for idx, char in enumerate(seq):
                for re in replacements:
                    if char != re:
                        new_seq = seq[:idx] + re + seq[idx + 1:]
                        if new_seq == end:
                            return level + 1
                        elif new_seq in bank:
                            bank.remove(new_seq)
                            q += [(new_seq, level + 1)]
        return -1