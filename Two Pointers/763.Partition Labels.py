from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance = {}
        for i, c in enumerate(s):
            last_appearance[c] = i

        l = 0
        res = []
        while l < len(s):
            start = l
            r = last_appearance[s[l]]
            while l <= r:
                if last_appearance[s[l]] > r:
                    r = last_appearance[s[l]]
                l += 1
            res += [r - start + 1]
        return res
