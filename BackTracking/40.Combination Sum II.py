from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self, candidates: List[int], target: int, start: int, path: List[int]):
        if target <= 0:
            if target == 0:
                self.res += [path]
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            else:
                self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])