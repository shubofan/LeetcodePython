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


class Solution:
	def longestSubstring(self, s: str, k: int) -> int:
		def check(cnt, k):
			for v in cnt.values():
				if v < k:
					return False

			return True

		n = len(s)
		if n < k:
			return 0
		res = 0

		# i is the most dinstint chars in subString
		for i in range(1, 27):
			l, r = 0, 0
			cnt = collections.Counter()
			while r < n:
				cnt[s[r]] += 1
				while l < r and len(cnt) > i:
					cnt[s[l]] -= 1
					if cnt[s[l]] == 0:
						cnt.pop(s[l])
					l += 1

				r += 1
				# s[l:r] is a candidate
				if len(cnt) == i and check(cnt, k):  # iff there are i distint chars and frequency of each >= k
					# print(r,l)
					res = max(res, r - l)

		return res

# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         if len(s) < k:
#             return 0
#         for char in set(s):
#             if s.count(char) < k:
#                 return max(self.longestSubstring(substr, k) for substr in s.split(char))