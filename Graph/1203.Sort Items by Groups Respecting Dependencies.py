import collections


class Solution:
	def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
		group2item = collections.defaultdict(set)
		for i in range(n):
			if group[i] == -1:
				group[i] = m
				m += 1
			group2item[group[i]].add(i)

		# find the relationships between the groups and each items in the same group
		# print(group2item)

		# Graph of items in the same graph
		t_g, t_in = collections.defaultdict(set), collections.defaultdict(int)

		# Graph, and in-degree among groups
		g_g, g_in = collections.defaultdict(set), collections.defaultdict(int)
		for i in range(n):
			# i, j in same group, j ->i
			for j in beforeItems[i]:
				if group[i] == group[j]:
					if i not in t_g[j]:
						t_g[j].add(i)
						t_in[i] += 1
				else:
					# j's group -> i's group
					if group[i] not in g_g[group[j]]:
						g_g[group[j]].add(group[i])
						g_in[group[i]] += 1

		# topological sort the groups
		groups_order = []

		q = collections.deque()

		for i in range(m):
			if i not in g_in:
				q += [i]

		while q:
			top = q.popleft()
			groups_order += [top]

			for nbr in g_g[top]:
				# print(nbr, top)
				if nbr in g_in:
					g_in[nbr] -= 1
					if g_in[nbr] == 0:
						g_in.pop(nbr)
						q += [nbr]

		if len(groups_order) != m:
			return []

		# topological sort the items in each group
		t_order = []
		for i in groups_order:
			items = group2item[i]

			q = collections.deque()
			lst = []
			for item in items:

				if item not in t_in:
					q += [item]

			while q:
				top = q.popleft()
				lst += [top]
				for nbr in t_g[top]:
					if nbr in t_in:
						t_in[nbr] -= 1
						if t_in[nbr] == 0:
							t_in.pop(nbr)
							q += [nbr]

			if len(lst) != len(items):
				return []
			t_order += lst[:]

		return t_order if len(t_order) == n else []


