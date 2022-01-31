# Time O(ElogE) in the heap where E is the length of times.  Dijkstra take (E+V) log(V) since E >> V so it can be E logE
# Space Complexity: O(N+E), the size of the graphO(E), plus the size of the dist objects used O(n).
import collections
import heapq


class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		g = collections.defaultdict(set)

		for i in range(len(times)):
			t = times[i]
			g[t[0]].add((t[1], t[2]))

		pq = []

		heapq.heappush(pq, (0, k))

		dist = {}  # <node: distance from k to node>
		while pq:
			step, cur = heapq.heappop(pq)
			if cur not in dist:  # cur node has been visited with the smallest distance from source
				dist[cur] = step
				for nbr, d2 in g[cur]:
					if nbr not in dist:
						heapq.heappush(pq, (d2 + step, nbr))

		if len(dist) < n:
			return -1

		return max(dist.values())