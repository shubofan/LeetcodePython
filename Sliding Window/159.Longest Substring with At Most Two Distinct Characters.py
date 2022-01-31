class Solution:
	"""
	@param s: a string
	@return: the length of the longest substring T that contains at most 2 distinct characters
	"""

	def lengthOfLongestSubstringTwoDistinct(self, s):
		n = len(s)
		if n < 3:
			return n

		# sliding window left and right pointers
		l, r = 0, 0

		# hashmap character -> its rightmost position
		# in the sliding window
		hashmap = {}

		max_len = 2

		while r < n:
			# when the slidewindow contains less than 3 characters
			hashmap[s[r]] = r
			r += 1

			# slide window contains 3 characters
			if len(hashmap) == 3:
				# delete the leftmost character
				del_idx = min(hashmap.values())
				hashmap.pop(s[del_idx])

				# move left pointer of the slide window
				l = del_idx + 1

			max_len = max(max_len, r - l)
		return max_len

# simple version. use 340: k distint, in this case k == 2
class Solution:
	"""
	@param s: a string
	@return: the length of the longest substring T that contains at most 2 distinct characters
	"""

	def lengthOfLongestSubstringTwoDistinct(self, s):
		n = len(s)
		if n < 3:
			return n

		cnt = collections.defaultdict(int)
		res = 0

		l, r = 0, 0
		while r < n:
			cnt[s[r]] += 1
			while len(cnt) > 2:
				cnt[s[l]] -= 1
				if cnt[s[l]] == 0:
					cnt.pop(s[l])
				l += 1

			res = max(res, r - l + 1)
			r += 1

		return res