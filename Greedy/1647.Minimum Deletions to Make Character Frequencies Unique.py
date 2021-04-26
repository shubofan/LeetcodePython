from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        fre = set()
        res = 0
        for char, n in cnt.items():
            while n in fre and n > 0:
                n -= 1
                res += 1
            fre.add(n)
        return res
