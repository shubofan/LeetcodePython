class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        l1 = 0
        l2 = 0

        while l1 < len(g) and l2 < len(s):
            if s[l2] >= g[l1]:
                l1 += 1
                l2 += 1
            else:
                l2 += 1

        return l1