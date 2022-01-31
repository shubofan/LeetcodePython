class Solution:
	def canConstruct(self, s: str, k: int) -> bool:
		if len(s) < k:
			return False

		cnt = collections.Counter(s)
		# a string can be a palindrome only if it has at most 1 character whose frequency is odd.
		odd_count = [value for value in cnt.values() if value % 2 == 1]

		odd_count_char = len(odd_count)

		if odd_count_char <= k:
			return True
		return False