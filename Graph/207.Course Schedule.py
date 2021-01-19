from collections import deque


class Node:
    def __init__(self, name: int):
        self.name = name
        self.outbound = []
        self.inbound = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        if not prerequisites:
            return True

        for i in range(0, numCourses):
            g[i] = Node(i)

        for edge in prerequisites:
            from_, to = edge[1], edge[0]

            from_node = g.get(from_)
            to_node = g.get(to)

            from_node.outbound += [to_node]
            to_node.inbound += [from_node]

        q = deque()
        sort = []
        for k, v in g.items():
            if not v.inbound:
                q.append(v)
        while q:
            top = q.popleft()
            sort += [top.name]
            out_nodes = top.outbound
            for node in out_nodes:
                node.inbound.remove(top)
                if not node.inbound:
                    q.append(node)

        return len(sort) == numCourses

