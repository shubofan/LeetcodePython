import collections
from typing import List


class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
		g = collections.defaultdict(set)
		dist = {}

		for f in flights:
			fro, target, price = f[0], f[1], f[2]
			g[fro].add((target, price))

		# min distance from src to i
		for i in range(n):
			dist[i] = float('inf')

		q = collections.deque()
		q += [[src, -1, 0]]  # (node, step, cost_so_far)

		while q:
			cur, step, cost = q.popleft()
			if step == k:
				continue
			for pair in g[cur]:
				nbr, price = pair[0], pair[1]
				if cost + price < dist[nbr]:
					dist[nbr] = cost + price
					q += [[nbr, step + 1, cost + price]]

		return dist[dst] if dist[dst] != float('inf') else -1

# 4.Dijkstra's (TLE)
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         g = collections.defaultdict(set)

#         for f in flights:
#             fro, target, price = f[0], f[1], f[2]
#             g[fro].add((target, price))

#         # for i in range(n):
#         #     dist[i] = float('inf')


#         pq = []
#         pq += [[0, src, k+1]]

#         while pq:
#             cost, cur, stop = heapq.heappop(pq)

#             if cur == dst:
#                 return cost
#             if stop <= 0:
#                 continue
#             for nbr, price in g[cur]:
#                 heapq.heappush(pq, [price+cost, nbr, stop-1])

#         return -1






