import collections
from typing import List


class Solution:
	# Time Complexity: O(∑ai LOG（ai）), where ai is the length of accounts[i] . Without the log factor, this is the complexity to build the graph and search for each component. The log factor is for sorting each component at the end.

	# Space Complexity: O(∑ai) the space used by our graph and our search.
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

		# {email: account name}
		em_to_name = {}
		graph = collections.defaultdict(set)

		# build graph
		for acc in accounts:
			name = acc[0]
			for idx, email in enumerate(acc[1:]):
				for idx2, email2 in enumerate(acc[idx + 1:]):
					graph[email2].add(email)
					graph[email].add(email2)
				em_to_name[email] = name
		res = []
		seen = set()

		# DFS
		for email in graph:
			if email not in seen:
				seen.add(email)
				stack = [email]
				component = []
				while stack:
					email = stack.pop()
					component += [email]
					for nbr in graph[email]:
						if nbr not in seen:
							seen.add(nbr)
							stack.append(nbr)
				component.sort()
				# add name to left most
				component.insert(0, em_to_name[email])
				res += [component]

		return res