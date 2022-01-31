from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(set)
        in_degree = {}
        n = len(words)
        for word in words:
            for c in word:
                in_degree[c] = 0

        for i in range(1, n):
            pre_word, nex_word = words[i - 1], words[i]
            l = min(len(pre_word), len(nex_word))
            for j in range(l):
                if pre_word[j] != nex_word[j]:
                    g[pre_word[j]].add(nex_word[j])
                    in_degree[nex_word[j]] += 1
                    break
        q = deque()
        for chr, degree in in_degree.items():
            if degree == 0:
                q.append(chr)
        res = []
        while q:
            top = q.popleft()
            res += [top]
            for nbr in list(g[top]):
                # g[top].remove(nbr)
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    q.append(nbr)

        if len(res) == len(in_degree):
            return ''.join(res)
        else:
            return ''

class Solution2:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c: [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # Step 2: Depth-first search.
        seen = {}  # False = grey, True = black.
        output = []

        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node]  # If this node was grey (False), a cycle was detected.
            seen[node] = False  # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False  # Cycle was detected lower down.
            seen[node] = True  # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)

if __name__ == '__main__':
    o = Solution()
    print(o.alienOrder(["wrt","wrf","er","ett","rftt"]))
    print(o.alienOrder(["z","x"]))
    print(o.alienOrder(["wrt","wrtz"]))
    print(o.alienOrder(["z","x", "z"]))

    o2 = Solution2()
    print(o2.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
    print(o2.alienOrder(["z", "x"]))
    print(o2.alienOrder(["wrt", "wrtz"]))
    print(o2.alienOrder(["z", "x", "z"]))