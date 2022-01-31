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
        # candidates  to be add from candidates[i:]
        for i in range(start, len(candidates)):
            # candidates[i] is not first to be add, and it == element added in path
            # example: first call self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])
            # then WILL NOT call self.dfs(candidates, target - candidates[i+1], i + 2, path + [candidates[i+1]])
            # if candidates[i+1] == candidates[i]
            if i != start and candidates[i] == candidates[i - 1]:
                continue
            else:
                self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])