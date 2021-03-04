class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count = 1  # n == 0
        used = [False] * 10
        for i in range(1, 10):
            used[i] = True
            count += self.dfs(i, used, n)
            used[i] = False
        return count

    def dfs(self, num: int, used: list[int], n: int) -> int:
        count = 0
        if num < 10 ** n:
            count += 1
        else:
            return count
        for i in range(10):
            if not used[i]:
                used[i] = True
                count += self.dfs(num * 10 + i, used, n)
                used[i] = False
        return count