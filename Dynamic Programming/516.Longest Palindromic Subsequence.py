class Solution:
	def longestPalindromeSubseq(self, s: str) -> int:
		n = len(s)
		dp = [[0] * n for _ in range(n)]

		# dp[i][j]: the longest palindromic subsequence's length of substring[i, j]
		for i in range(n):
			dp[i][i] = 1

		# diff = j - i i.e. length of substring[i, j]
		for diff in range(1, n):
			for i in range(n - diff):
				j = i + diff
				if s[i] == s[j]:
					dp[i][j] = dp[i + 1][j - 1] + 2
				else:
					dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

		return dp[0][-1]
