import collections


class Solution:
	"""
	@param n: An integer
	@param edges: a list of undirected edges
	@return: true if it's a valid tree, or false
	"""

	def validTree(self, n, edges):
		# Check whether or not there are n - 1 edges. If there's not, then return false .
		# Check whether or not the graph is fully connected . Return true if it is, false if otherwise.
		g = collections.defaultdict(set)
		if len(edges) != n - 1:
			return False

		for edge in edges:
			g[edge[0]].add(edge[1])
			g[edge[1]].add(edge[0])
		stack = [0]
		seen = set()
		seen.add(0)
		res = []

		while stack:
			cur = stack.pop()

			for nbr in g[cur]:
				if nbr not in seen:
					stack += [nbr]
					seen.add(nbr)

		return len(seen) == n