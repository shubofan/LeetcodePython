import collections
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        g = collections.defaultdict(set)

        for p in prerequisites:
            g[p[1]].add(p[0])
            indegree[p[0]] += 1

        q = collections.deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q += [i]

        res = []

        while q:
            node = q.popleft()
            res += [node]
            for nbr in g[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q += [nbr]

        # len(res) == numCourses means there is a valid topological sort else, there is a cycle so return []
        return res if len(res) == numCourses else []