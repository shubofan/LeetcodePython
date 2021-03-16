from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = [0] * 26
        s_cnt = [0] * 26

        for c in p:
            p_cnt[ord(c) - 97] += 1

        l, r = 0, 0
        res = []

        while r < len(s):
            if r < len(p) - 1:
                s_cnt[ord(s[r]) - 97] += 1
                r += 1
                continue

            s_cnt[ord(s[r]) - 97] += 1
            if s_cnt == p_cnt:
                res += [l]
            s_cnt[ord(s[l]) - 97] -= 1
            r += 1
            l += 1

        return res