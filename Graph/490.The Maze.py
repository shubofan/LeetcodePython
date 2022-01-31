# Time complexity : O(mn). Complete traversal of maze will be done in the worst case. Here, m and n refers to the number of rows and coloumns of the maze.

# Space complexity : O(1)


class Solution:
	"""
	@param maze: the maze
	@param start: the start
	@param destination: the destination
	@return: whether the ball could stop at the destination
	"""

	def hasPath(self, maze, start, destination):
		def dfs(maze, x, y, dx, dy):

			dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
			m, n = len(maze), len(maze[0])
			if dx == x and dy == y:
				return True

			maze[x][y] = -1  # mark to -1 to indicate (x, y) has been visited
			for d in dirs:
				nx, ny = x, y
				while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1:  # ball keeps rolling until meeting the wall
					nx += d[0]
					ny += d[1]

				# back to the stop point
				nx -= d[0]
				ny -= d[1]

				if maze[nx][ny] != -1:
					if dfs(maze, nx, ny, dx, dy):
						return True
			return False

		return dfs(maze, start[0], start[1], destination[0], destination[1])