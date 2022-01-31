class Solution:

    # 两个指针l和r. l代表着目前lexicographical order最大的substring的起点. r作为遍历指针, 用来找可能比i所代表的的substring更大的substring.
    # l起始值为0, r为1. 表示以0开始的substring和以1开始的substring比大小.
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        l, r = 0, 1
        step = 0
        while r + step < n:
            if s[l + step] == s[r + step]:
                step += 1
            elif s[l + step] < s[r + step]:  # current substring start from r is larger, update l = l + step + 1
                l = l + step + 1
                r = l + 1
                step = 0
            elif s[l + step] > s[r + step]:  # # try to find larger new sub-string start from r+step+1
                r = r + step + 1
                step = 0

        return s[l:]


class Solution:
    def lastSubstring(self, s: str) -> str:
        self.res = set()

        for i in range(len(s)):
            self.dfs(s, i, '')
        return sorted(list(self.res))[-1]

    def dfs(self, s, start, path):
        self.res.add(path)

        if start == len(s):
            return

        self.dfs(s, start + 1, path + s[start])