#  Time: O(ElogE)  heappush for each edge O(ElogE) + heappop for each edge O(ElogE) -> O(ElogE) in total
#  Space: O(E)
import collections, heapq


class Solution:
	def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

		g = collections.defaultdict(set)
		for e in edges:
			g[e[0]].add((e[1], e[2]))
			g[e[1]].add((e[0], e[2]))

		dist = {i: float('inf') for i in range(n + 1)}
		dist[n] = 0

		pq = []
		ways = [0] * (n + 1)  # ways[i] -> restricted path from n to i
		ways[-1] = 1
		heapq.heappush(pq, (0, n))

		while pq:
			step, cur = heapq.heappop(pq)
			if dist[cur] < step:
				continue
			for nbr, w in g[cur]:
				if step + w < dist[nbr]:
					dist[nbr] = step + w
					heapq.heappush(pq, (dist[nbr], nbr))
				if dist[cur] > dist[nbr]:
					ways[cur] = (ways[nbr] + ways[cur]) % (10 ** 9 + 7)

		return ways[1]

