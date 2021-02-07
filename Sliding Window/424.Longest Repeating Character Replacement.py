class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        res = 0
        l, n = 0, len(s)
        r = l
        maxCount = 0

        # [left, right] 内最多替换 k 个字符可以得到只有一种字符的子串
        while r < n:
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxCount = max(maxCount, cnt[s[r]])

            if maxCount + k < r - l + 1:
                cnt[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return res