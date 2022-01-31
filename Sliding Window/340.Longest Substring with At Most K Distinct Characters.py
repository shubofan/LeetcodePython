
# O(n)
import collections


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):

        cnt = collections.defaultdict(int)
        res = 0
        n = len(s)
        l, r = 0, 0
        while r < n:
            cnt[s[r]] += 1
            while len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstringKDistinct("eceba", 2))
    print(s.lengthOfLongestSubstringKDistinct("aa", 1))
    print(s.lengthOfLongestSubstringKDistinct("abcdef", 6))
    print(s.lengthOfLongestSubstringKDistinct("abcdef", 1))
    print(s.lengthOfLongestSubstringKDistinct("aaaaa", 1))
    print(s.lengthOfLongestSubstringKDistinct("aaaaa", 0))