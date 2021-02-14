from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        if not graph:
            return self.res
        self.dfs(graph, 0, [0])
        return self.res

    def dfs(self, graph: List[List[int]], start: int, path: List[int]) -> None:
        n = len(graph)
        if start == n - 1:
            self.res += [path]
            return
        if start == n:
            return
        neighbors = graph[start]
        for neighbor in neighbors:
            self.dfs(graph, neighbor, path + [neighbor])


