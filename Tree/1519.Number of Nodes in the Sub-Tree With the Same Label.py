# post_order_traverse
# Time O(E+V), E is the number of Nodes, V is number of Edges
# Space: O(E + V)
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        n = len(labels)
        self.res = [0] * n
        seen = set()
        g = collections.defaultdict(set)

        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])


        # for current node, count[i] means for label i, all count of label i in the sub-tree of this node.
        def post_order_traverse(g, labels, node, seen, count):
            if node in seen:
                return
            seen.add(node)

            before = count[ord(labels[node]) - ord('a')]
            for child in g[node]:
                post_order_traverse(g, labels, child, seen, count)

            count[ord(labels[node]) - ord('a')] += 1
            self.res[node] = count[ord(labels[node]) - ord('a')]  - before

        post_order_traverse(g, labels, 0, seen, [0] * 26)
        return self.res


# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         n = len(labels)
#         self.res = [0] * n
#         g = collections.defaultdict(set)

#         for e in edges:
#             g[e[0]].add(e[1])
#             g[e[1]].add(e[0])


#         def dfs(g, labels, node, parent):
#             cnt = collections.Counter()
#             for child in g[node]:
#                 if child != parent:
#                     cnt += dfs(g, labels, child, node)

#             cnt[labels[node]] += 1
#             self.res[node] = cnt[labels[node]]
#             return cnt

#         dfs(g, labels, 0, None)
#         return self.res