from typing import List
#  DFS Solution
#  Time complexity: O(N^2) # the entire graph need to be visited
#  Space complexity: O(N^2)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {} # {1: [2]}
        seen = set()
        res = 0

        # construct the graph {city: neighbours without itself}
        for city, nbrs in enumerate(isConnected):
            graph[city] = []
            for idx, nbr in enumerate(nbrs):
                if idx != city and nbr == 1:
                    graph[city].append(idx)

        # for each city that has not been searched, start dfs to find a Connected component
        for k, v in graph.items():
            if k not in seen:
                res += 1
                stack = [k]
                while stack:
                    city = stack.pop()
                    for nbr in graph[city]:
                        if nbr not in seen:
                            stack.append(nbr)
                            seen.add(nbr)

        return res
