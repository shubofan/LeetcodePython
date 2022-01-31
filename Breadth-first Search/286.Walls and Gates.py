import collections
# Time complexity : O(mn)

# Let us start with the case with only one gate. The breadth-first search takes at most m×n steps to reach all rooms, therefore the time complexity is O(mn).
# But what if you are doing breadth-first search from k gates?

# Once we set a room's distance, we are basically marking it as visited, which means each room is visited at most once.
# Therefore, the time complexity does not depend on the number of gates and is O(mn)



#Space complexity : O(mn). The space complexity depends on the queue's size. We insert at most m×n points into the queue.

class Solution:
	"""
	@param rooms: m x n 2D grid
	@return: nothing
	"""

	def wallsAndGates(self, rooms):
		m, n = len(rooms), len(rooms[0])

		q = collections.deque()
		seen = set()

		# start from all gates, and update update the distance to an empty room in each level
		for x in range(m):
			for y in range(n):
				if rooms[x][y] == 0:
					q.append((x, y))
					seen.add((x, y))
		dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

		while q:
			x, y = q.popleft()

			for d in dirs:
				nx, ny = x + d[0], y + d[1]
				if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] > 0 and (nx, ny) not in seen:
					q.append((nx, ny))
					seen.add((nx, ny))
					rooms[nx][ny] = rooms[x][y] + 1



class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    # DFS
    def wallsAndGates(self, rooms):
        def dfs(rooms, x, y, distance):
            m , n = len(rooms), len(rooms[0])
            if 0 <=x<m and 0<=y< n and rooms[x][y] >= distance:
                rooms[x][y] = distance
                dfs(rooms, x+1, y, distance+1)
                dfs(rooms, x-1, y, distance+1)
                dfs(rooms, x, y+1, distance+1)
                dfs(rooms, x, y-1, distance+1)
        m , n = len(rooms), len(rooms[0])
        for x in range(m):
            for y in range(n):
                if rooms[x][y] == 0:
                    dfs(rooms, x, y, 0)