from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for edge in edges:
            v1, v2 = edge[0], edge[1]
            g[v1].append(v2)
            g[v2].append(v1)

        leaves = deque()
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        for k, v in g.items():
            if len(v) == 1:
                leaves.append(k)

        remain_nodes = n

        # BFS from leaf to central, until there are at most 2 nodes that have not been visted
        # level order bfs, each time all the leaves in the queue 
        while remain_nodes > 2:
            size = len(leaves)
            remain_nodes -= size

            while size > 0:
                leaf = leaves.popleft()
                for neighbour in g[leaf]:
                    g[neighbour].remove(leaf)
                    # if leaf's neighbour becomes a leaf, add it to  queue leaves
                    if len(g[neighbour]) == 1:
                        leaves.append(neighbour)
                size -= 1
        return list(leaves)
