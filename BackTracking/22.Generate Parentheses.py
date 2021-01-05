class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(n, '')
        return self.res

    def dfs(self, n: int, path: str) -> None:
        if len(path) == 2 * n:
            self.res += [path]
            return
        # first element must be '('
        if len(path) == 0:
            self.dfs(n, path + '(')
        # last element must be ')'
        elif len(path) == 2 * n - 1:
            self.dfs(n, path + ')')
        else:
            # if count of '(' is less than n, we can add '('
            if path.count('(') != n:
                self.dfs(n, path + '(')
            # if count of ')' is less than '(', we can add ')'
            if path.count('(') > path.count(')'):
                self.dfs(n, path + ')')
