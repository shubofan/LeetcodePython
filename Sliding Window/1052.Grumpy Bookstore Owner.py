from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        res = 0
        max_extra = 0  # max_extra if overwrite X '1's in the window
        extra = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0: # just take it into sum
                res += customers[i]  # get sum when owner isn't grumpy cause this is what greedy looks like

            if grumpy[i] == 1:
                extra += customers[i]  # include in window even it is one

            if i >= X and grumpy[i - X] == 1:  # slide window to right if reach the window's limit
                extra -= customers[i - X]

            max_extra = max(max_extra, extra)  # maintain max extra
        return res + max_extra
