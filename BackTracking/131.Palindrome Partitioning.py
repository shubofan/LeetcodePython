# Time Complexity : (N⋅2N), where N is the length of string s.
# This is the worst-case time complexity when all the possible substrings are palindrome.  like aaa


# Total 2^N possible sub-strings and each of which took O(N) to check is Palindrome, so in total O(N * 2^N)


from typing import List


class Solution:
	def partition(self, s: str) -> List[List[str]]:
		def helper(s, start, path):
			if start == len(s):
				self.res += [path[:]]
				return

			for i in range(start + 1, len(s) + 1):
				if s[start: i] == s[start: i][::-1]:
					helper(s, i, path + [s[start:i]])

		self.res = []
		helper(s, 0, [])
		return self.res