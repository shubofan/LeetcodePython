import collections, heapq
from typing import List


class Solution:
	def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
		g = collections.defaultdict(set)
		dist = {}  # <node, max probability from start to this node>

		for idx, edge in enumerate(edges):
			g[edge[0]].add((edge[1], succProb[idx]))
			g[edge[1]].add((edge[0], succProb[idx]))

		pq = []

		heapq.heappush(pq, (-1.0,
		                    start))  # max heap since we need to store tuple (max probability from start node to current node, current node)

		while pq:
			probability, node = heapq.heappop(pq)

			# if current node has max probability, discard this since it must smaller than value in dist
			if node in dist:
				continue

			dist[node] = probability

			for nbr in g[node]:
				heapq.heappush(pq, (probability * nbr[1], nbr[0]))

		if end in dist:
			return dist[end] * -1
		# no path form start to end
		else:
			return 0