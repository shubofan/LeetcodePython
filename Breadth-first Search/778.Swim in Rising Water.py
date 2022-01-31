class Solution:
	# Dijkstra using Priority Queue, O(n^2*logn), 20 ms;
	# In every step, find lowest water level to move forward, so using PQ rather than queue
	def swimInWater(self, grid: List[List[int]]) -> int:
		n = len(grid)
		start = (0, 0)
		pq = []
		res = 0
		heapq.heappush(pq, (grid[0][0], start))

		visited = set()
		visited.add(start)
		dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
		while pq:
			distance, point = heapq.heappop(pq)
			x, y = point[0], point[1]

			res = max(res, distance)
			if x == y == n - 1:
				return res
			for d in dirs:
				nx, ny = x + d[0], y + d[1]
				if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
					heapq.heappush(pq, (grid[nx][ny], (nx, ny)))
					visited.add((nx, ny))

		return -1
