class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        # limit the total number diff char appears in window <= i
        for i in range(1, 27):
            l, r = 0, 0
            # total count of char in the window, total count of char whose frequency >=k in the window
            diff_char_cnt, char_cnt_greater_than_k = 0, 0
            counter = [0] * 26
            while r < len(s):
                # Expand the window by moving right
                char = s[r]
                idx = ord(char) - 97
                counter[idx] += 1
                if counter[idx] == 1:
                    diff_char_cnt += 1
                if counter[idx] == k:
                    char_cnt_greater_than_k += 1
                r += 1

                # shrink the window from left to ensure there are no more than i char in the window
                while l < r and diff_char_cnt > i:
                    char = s[l]
                    idx = ord(char) - 97
                    counter[idx] -= 1

                    if counter[idx] == 0:
                        diff_char_cnt -= 1

                    if counter[idx] == k - 1:
                        char_cnt_greater_than_k -= 1
                    l += 1

                # each char in the window appears more than k times, so the window is valid
                if char_cnt_greater_than_k == i == diff_char_cnt:
                    res = max(res, r - l)
        return res
