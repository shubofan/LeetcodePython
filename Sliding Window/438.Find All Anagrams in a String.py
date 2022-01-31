from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # o(1)
        p_cnt = Counter(p)
        s_cnt = Counter()

        l, r = 0, 0
        res = []
        #Time Complexity - O(S)
        # Each array element element would be traversed at most twice.

        #Space complexity - O(1)
        #Since we are using constant extra space (map) of size 26
        while r < len(s):
            s_cnt[s[r]] += 1
            # s[l:r+1] is anagram
            if r - l == len(p) - 1:
                if p_cnt == s_cnt:
                    res += [l]
                s_cnt[s[l]] -= 1
                if s_cnt[s[l]] == 0:
                    s_cnt.pop(s[l])
                l += 1
            r += 1
        return res