class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        # O(n * (2n + 1)) = O(n^2)
        for i in range(n):
            res += self.expand(s, i, i)
            res += self.expand(s, i, i + 1)
        return res

    def expand(self, s: str, l: int, r: int) -> int:
        res = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            else:
                break
        return res
