# from collections import defaultdict
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         n = len(tickets)


#         g = defaultdict(list)

#         res = []

#         if not tickets:
#             return ["JFK"]
#         for ticket in tickets:
#             g[ticket[0]].append(ticket[1])
#             g[ticket[0]] = sorted(g[ticket[0]])

#         s = ["JFK"]
#         while s:
#             nbr = g[s[-1]]
#             while nbr:
#                 print(s)
#                 s.append(nbr.pop(0))
#                 nbr = g[s[-1]]

#             # The first elements canoot go back, so it need to placed at last
#             res.insert(0, s.pop())
#         return res
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        self.g = defaultdict(list)

        self.res = []

        if not tickets:
            return ["JFK"]
        for ticket in tickets:
            self.g[ticket[0]].append(ticket[1])

        s = ["JFK"]
        self.dfs("JFK", tickets, ["JFK"])

        return self.res

    def dfs(self, cur: str, tickets: List[List[str]], path: List[str]) -> bool:
        if len(path) == len(tickets) + 1:
            self.res = path
            return True
        self.g[cur] = sorted(self.g[cur])

        for _ in self.g[cur]:
            to = self.g[cur].pop(0)

            if self.dfs(to, tickets, path + [to]):
                return True
            else:
                self.g[cur].append(to)
        return False
