# Kruskal to get minimum spanning tree

class Solution:
	def minimumCost(self, N: int, connections: List[List[int]]) -> int:
		parent = [0] * (N + 1)
		for i in range(1, N + 1):
			parent[i] = i

		def find(a, parent):
			if parent[a] != a:
				parent[a] = find(parent[a], parent)
			return parent[a]

		def union(a, b):
			pa = find(a, parent)
			pb = find(b, parent)
			if pa != pb:
				parent[pb] = pa

		connections.sort(key=lambda x: x[2]) # sort against cost
		total_cost = 0
		cnt = 0

		for con in connections:

			p0 = find(con[0], parent)
			p1 = find(con[1], parent)
			# not same parent, so union p0 and p1
			if p0 != p1:
				parent[p1] = p0
				cnt += 1 # num of connected edges
				total_cost += con[2]

		if cnt < N - 1:
			return -1
		else:
			return total_cost