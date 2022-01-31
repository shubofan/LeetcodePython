class Solution:

	# dp[i][j], playlist length is i and it contains j different songs

	# for dp[i][j]。if we want add new song: it has dp[i-1][j-1] * (n - j + 1) ways.
	# if we want to chose a old song has been played before，dp[i-1][j] * max(j-K, 0)（j 首歌，最近的 K 首不可以播放）。

	def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
		dp = [[0] * (n + 1) for _ in range(goal + 1)]

		dp[0][0] = 1

		for i in range(1, goal + 1):
			for j in range(1, n + 1):
				dp[i][j] += dp[i - 1][j - 1] * (n - j + 1)  # dp[1][1] = 1 * (n - 1 + 1) -> n songs to be picked up.
				dp[i][j] += dp[i - 1][j] * max(j - k, 0)
				dp[i][j] %= 10 ** 9 + 7
		return dp[-1][-1]
