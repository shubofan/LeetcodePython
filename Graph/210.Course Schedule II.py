from collections import deque


class Node:
    def __init__(self, name: int):
        self.name = name
        self.outbound = []
        self.inbound = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        g = {}
        q = deque()
        sort = []

        # Create graph
        for i in range(0, numCourses):
            g[i] = Node(i)

        for edge in prerequisites:
            from_, to = edge[1], edge[0]

            from_node = g.get(from_)
            to_node = g.get(to)

            from_node.outbound += [to_node]
            to_node.inbound += [from_node]

            # topological sort
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

        # len(sort) == numCourses means there is a valid topological sort else, there is a cycle so retrun []
        return sort if len(sort) == numCourses else []
