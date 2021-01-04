from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i] means if sub string: s[:i] can be broken down
        dp = [False] * (n + 1)
        dp[0] = True  # dp[0] is ''

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
        return dp[-1]
