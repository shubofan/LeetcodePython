import collections


class Solution:
	def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

		d_red = collections.defaultdict(list)
		for e in red_edges:
			d_red[e[0]].append(e[1])

		d_blue = collections.defaultdict(list)
		for e in blue_edges:
			d_blue[e[0]].append(e[1])

		answer = [float("inf")] * n

		depth = 0
		q = collections.deque()
		q += [(0, True, depth), (0, False, depth)]

		visted_red = set()
		visted_blue = set()
		while q:
			v, red, depth = q.popleft()

			answer[v] = min(answer[v], depth)

			if red:
				visted_red.add(v)
				for i in d_blue[v]:
					if i not in visted_blue:
						q.append((i, not red, depth + 1))
			else:
				visted_blue.add(v)
				for i in d_red[v]:
					if i not in visted_red:
						q.append((i, not red, depth + 1))

		for i in range(len(answer)):
			if answer[i] == float("inf"):
				answer[i] = -1

		return answer