from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        lst = [x for x in range(1, 10)]
        self.dfs(lst, [], 0, k, n)
        return self.res

    def dfs(self, lst: List[int], path: List[int], start: int, k: int, n: int):
        if len(path) == k and sum(path) == n:
            self.res += [path]
            return
        elif len(path) > k or sum(path) > n:
            return
        else:
            # put lst[i] to path, start to dfs from lst[i + 1]
            for i in range(start, len(lst)):
                self.dfs(lst[:i] + lst[i + 1:], path + [lst[i]], i, k, n)
            set
