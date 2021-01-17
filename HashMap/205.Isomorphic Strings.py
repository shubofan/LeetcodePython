from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = defaultdict(list)
        dic2 = defaultdict(list)

        for i in range(len(s)):
            dic1[s[i]] += [i]
            dic2[t[i]] += [i]

        for vals in dic1.values():
            if vals not in dic2.values():
                return False
        return True
