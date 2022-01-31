import heapq

#Time complexity : O(mn∗log(mn)). 
# v = m*n (vertices in total in the maze), Dijkstra take (v+e)logv -> mn*log(mn)

# Space complexity : O(mn) distance array of size m*n is used.

class Solution:
	"""
	@param maze: the maze
	@param start: the start
	@param destination: the destination
	@return: the shortest distance for the ball to stop at the destination
	"""

	def shortestDistance(self, maze, start, destination):
		dist = {}
		m, n = len(maze), len(maze[0])
		pq = []
		heapq.heappush(pq, (0, (start[0], start[1])))
		dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], ]
		while pq:
			dis, t = heapq.heappop(pq)

			x, y = t[0], t[1]
			if (x, y) in dist:
				continue
			dist[(x, y)] = dis

			for d in dirs:
				nx, ny = x, y
				cnt = 0
				while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1:
					nx += d[0]
					ny += d[1]
					cnt += 1

				nx -= d[0]
				ny -= d[1]
				cnt -= 1
				heapq.heappush(pq, ((dis + cnt, (nx, ny))))

		if (destination[0], destination[1]) in dist:
			return dist[(destination[0], destination[1])]

		return -1


# Description
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
#
# You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
# 1.There is only one ball and one destination in the maze.
# 2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# 3.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.