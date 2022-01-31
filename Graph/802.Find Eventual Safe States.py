from typing import List


class Solution:
	# Reverse the graph and do topological sort
	# terminal node -> if there are no incoming edges
	# A node is a safe node -> from any terminal node can lead to this node

	# 时间复杂度：O(n+m)，其中 n 是图中的点数，m 是图中的边数。

	# 空间复杂度：O(n+m)。需要 O(n+m) 的空间记录反图。

	#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
	#         n = len(graph)
	#         g = collections.defaultdict(set)
	#         indegree = [0] * n
	#         res = []
	#         for i, nbrs in enumerate(graph):
	#             for nbr in nbrs:
	#                 g[nbr].add(i)
	#                 indegree[i] += 1

	#         q = collections.deque()

	#         # push all  terminal node to queue
	#         for i in range(n):
	#             if indegree[i] == 0:
	#                 q += [i]

	#         while q:
	#             node = q.popleft()
	#             res += [node]

	#             for nbr in g[node]:
	#                 indegree[nbr] -= 1
	#                 if indegree[nbr] == 0:
	#                     q += [nbr]
	#         return sorted(res)

	# DFS
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		n = len(graph)

		# record status for each node
		status = [0] * n  # 0 not visited, 1 visited, 2 finish search, and safe

		def safe(i):  # determine if a node is safe
			if status[i] > 0:
				return status[i] == 2

			status[i] = 1
			for nbr in graph[i]:
				if not safe(nbr):  # meet a node of with status of 1 -> find a cycle,
					return False
			status[i] = 2  # no outgoing edges or every possible path starting from that node leads to a terminal node
			return True

		return [i for i in range(n) if safe(i)]

# 根据题意，若起始节点位于一个环内，或者能到达一个环，则该节点不是安全的。否则，该节点是安全的。

# 我们可以使用深度优先搜索来找环，并在深度优先搜索时，用三种颜色对节点进行标记，标记的规则如下：

#     白色（用 0 表示）：该节点尚未被访问；
#     灰色（用 1 表示）：该节点位于递归栈中，或者在某个环上；
#     黑色（用 2 表示）：该节点搜索完毕，是一个安全节点。

# 当我们首次访问一个节点时，将其标记为灰色，并继续搜索与其相连的节点。

# 如果在搜索过程中遇到了一个灰色节点，则说明找到了一个环，此时退出搜索，栈中的节点仍保持为灰色，这一做法可以将「找到了环」这一信息传递到栈中的所有节点上。

# 如果搜索过程中没有遇到灰色节点，则说明没有遇到环，那么递归返回前，我们将其标记由灰色改为黑色，即表示它是一个安全的节点。

# 时间复杂度：O(n+m)，其中 n 是图中的点数，m 是图中的边数。

# 空间复杂度：O(n)。存储节点颜色以及递归栈的开销均为 O(n)。


