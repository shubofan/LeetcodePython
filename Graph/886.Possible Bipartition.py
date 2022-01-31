import collections
from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        self.partable = True
        for dislike in dislikes:
            a, b = dislike[0], dislike[1]
            g[a].append(b)
            g[b].append(a)

        # 用来标记每一个节点的颜色，true 是一种颜色， false 是一种颜色
        color = [False] * (N + 1)
        visited = [False] * (N + 1)
        for i in range(1, N + 1):
            if not visited[i]:
                self.dfs(i, g, color, visited)
            if not self.partable:
                return False
        return True

    def dfs(self, i: int, g: dict, color: List[bool], visited: List[bool]):
        visited[i] = True
        for neighbor in g[i]:
            if not visited[neighbor]:
                # mark different color
                color[neighbor] = not color[i]
                self.dfs(neighbor, g, color, visited)
            # 如果发现访问过 neighbor 节点，但是 neighbor 节点和 i 节点是一样的颜色了,
            # 那么说明图中有两个相邻节点不能染成两种颜色
            elif color[i] == color[neighbor]:
                self.partable = False


class Solution:
    # Time Complexity: O(N+E), where E is the length of dislikes . DFS takes O(N + E)
    # Space Complexity: O(N+E). map g takes O(N + E)

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = collections.defaultdict(set)
        for dislike in dislikes:
            g[dislike[0]].add(dislike[1])
            g[dislike[1]].add(dislike[0])
        self.visited = set()
        # for each node, it could either be marked as color True or color not

        self.colors = {}  # <node, color>
        for i in range(1, n + 1):
            if i not in self.visited:
                if not self.part(i, g, False):
                    return False
        return True

    def part(self, i, g, color):
        self.visited.add(i)
        self.colors[i] = color

        for nbr in g[i]:
            if nbr not in self.visited:
                # mark neighbors to negated color
                if not self.part(nbr, g, not color):
                    return False
            else:
                # a neighbor has been marked as same color, cannot partion
                if self.colors[nbr] == self.colors[i]:
                    return False
        return True
