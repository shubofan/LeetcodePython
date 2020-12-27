class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        res = 0

        if not s:
            return res
        lst = list(s)

        dic = {}

        while l < len(lst) and r < len(lst):
            if lst[r] not in dic or dic[lst[r]] == 0:
                dic[lst[r]] = 1
                r += 1
                res = max(res, r - l)
            else:
                dic[lst[l]] = 0
                l += 1
        return res
