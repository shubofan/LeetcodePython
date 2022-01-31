# Time Complexity: O(N^3), where N is the length of grid . Our dynamic programming has O(N3) states.

# Space Complexity: O(N^3), the size of dp .
# 正确的做法是让两个人同时从左上走到右下（或从右下走到左上），乍看起来是一个四维的动态规划问题, dp[x1][y1][x2][y2]分别表示从第一个人从左上走到(x1, y1)且第二个人从左上走到(x2, y2)的最大樱桃数，但是由于两个人是同步走的，因此x1 + y1 = x2 + y2，实际只有3个自由变量，是三维动态规划dp[x1][y1][x2]. 状态转移的时候注意判断状态不可达的情况

class Solution:
	def cherryPickup(self, grid: List[List[int]]) -> int:
		n = len(grid)
		self.dp = [[[0] * n for _ in range(n)] for i in range(n)]

		# Two people start from (0, 0) to (n - 1, n - 1)
		# dp[x1][y1][x2] be the most number of cherries obtained by two people starting at (x1, y1) and (x2, y2)

		def get_dp(grid, x1, y1, x2):
			y2 = x1 + y1 - x2
			n = len(grid)

			# position does not exist
			if x1 >= n or x2 >= n or y1 >= n or y2 >= n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
				return float('-inf')

			if x1 == y1 == n - 1:
				return grid[x1][y1]

			if self.dp[x1][y1][x2] != 0:
				return self.dp[x1][y1][x2]

			# if person1 and person2 at same position, just collect 1 cheery
			res = grid[x1][y1] if (x1 == x2) else grid[x1][y1] + grid[x2][y2]
			# 4 case: person1 and person2 go right , person1 go down and person2 go right, person1 and person2 go down, person1 go right and person2 go down
			res += max(get_dp(grid, x1, y1 + 1, x2), get_dp(grid, x1 + 1, y1, x2), get_dp(grid, x1 + 1, y1, x2 + 1),
			           get_dp(grid, x1, y1 + 1, x2 + 1))
			self.dp[x1][y1][x2] = res
			return res

		return max(0, get_dp(grid, 0, 0, 0))
