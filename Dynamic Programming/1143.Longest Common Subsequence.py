class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		#  a b c
		# a 1 1 1
		# b 1 2 2
		# c 1 2 3

		'''
		dp(i,j) means the longest common subsequence of text1[:i] and text2[:j].
		If text1[i]==text2[j], then dp(i,j) should equal dp(i-1,j-1)+1
		Otherwise, dp(i,j)=max(dp(i-1,j), dp(i,j-1))
		'''

		n1, n2 = len(text1), len(text2)

		dp = [[0] * (n2 + 1) for i in range(n1 + 1)]

		for i in range(1, n1 + 1):
			for j in range(1, n2 + 1):
				if text1[i - 1] == text2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

		return dp[-1][-1]