class Solution:
	def kthSmallest(self, mat: List[List[int]], k: int) -> int:
		m, n = len(mat), len(mat[0])

		# pq stores pair (the corresponding sum, column index of each row)
		pq = []

		res = 0
		cols = []
		visited = set()
		sum_ = 0

		for i in range(m):
			cols += [0]
			sum_ += mat[i][0]

		heapq.heappush(pq, (sum_, cols))
		visited.add(tuple(cols))

		while pq:
			sum_, cols = heapq.heappop(pq)
			k -= 1
			if k == 0:
				return sum_

			for row, col in enumerate(cols):
				if col + 1 < n:
					new_sum = sum_ - mat[row][col] + mat[row][col + 1]
					new_cols = cols[:]
					new_cols[row] = col + 1
					if tuple(new_cols) not in visited:
						heapq.heappush(pq, (new_sum, new_cols))
						visited.add(tuple(new_cols))

		return res