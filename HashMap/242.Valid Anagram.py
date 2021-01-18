class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        d1, d2 = {}, {}
        for i in range(ls):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1

        for k, v in d1.items():
            if k not in d2:
                return False
            if d2[k] != v:
                return False
        return True

        # return sorted(s) == sorted(t)