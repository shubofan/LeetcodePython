class UnionFind:
	def __init__(self):
		self.parent = {}  # <(x, y), parent>
		self.components = 0  # number un-connected components

	def init(self, n):  # At first each point is a sepratate component
		for i in range(1, n + 1):
			self.parent[i] = i
			self.components += 1

	def find(self, x):
		if x == self.parent[x]:
			return x
		self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		rootX, rootY = self.find(x), self.find(y)

		if rootX == rootY:  # if x and y has alreay connected
			return False
		self.parent[rootX] = rootY  # connect x and y
		self.components -= 1  # number of un-connected components - 1
		return True


class Solution:
	def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
		edges.sort(key=lambda x: (-x[0], x[1], x[2]))  # sort to make type 3 at first
		A = UnionFind()
		B = UnionFind()
		A.init(n)
		B.init(n)

		edgeAdded = 0  # number of edges to be added to make the Graph Fully Traversable

		for edge in edges:
			typ, u, v = edge[0], edge[1], edge[2]
			if typ == 3:  # connect (u, v) for both A and B
				a = A.union(u, v)
				b = B.union(u, v)
				# DON't use: if A.union() or B.union() since B.union() may not be run due to short circuit
				if a or b:  # Don't add edge when (u,v) has been connected for BOTH A and B
					edgeAdded += 1

			if typ == 2:
				if B.union(u, v):
					edgeAdded += 1
			if typ == 1:
				if A.union(u, v):
					edgeAdded += 1

		if A.components == 1 and B.components == 1:  # If Both A and B fully connected, get number of edges to be removed
			return len(edges) - edgeAdded
		return -1