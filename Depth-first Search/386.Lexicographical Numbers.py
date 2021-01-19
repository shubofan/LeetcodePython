from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.res = []
        for i in range(1, 10):
            self.dfs(n, i)
        return self.res

    def dfs(self, n: int, cur: str):
        if int(cur) > n:
            return
        self.res += [int(cur)]
        for i in range(10):
            self.dfs(n, cur * 10 + i)
