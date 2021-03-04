class Solution:
    def grayCode(self, n: int) -> List[int]:
        self.res = []
        self.dfs(n, '', '0')
        return self.res

    def dfs(self, n: int, path: str, elementToBeAddNext: str) -> None:
        if len(path) == n:
            self.res += [int(path, 2)]
            return
        if elementToBeAddNext == '0':
            self.dfs(n, path + '0', '0')
            self.dfs(n, path + '1', '1')
        else:
            self.dfs(n, path + '1', '0')
            self.dfs(n, path + '0', '1')