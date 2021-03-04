import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        if H <= len(piles):
            return r

        def get_total(speed: int):
            total = 0
            for pile in piles:
                total += (math.ceil(pile / speed))
            return total

        while l < r:
            mid = (l + r) // 2
            total = get_total(mid)
            if total > H:
                l = mid + 1
            else:
                r = mid
        return l