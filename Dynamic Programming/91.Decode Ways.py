class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # dp[0] means an empty string will have one way to decode, dp[1] means the way to decode a string of size 1
        dp = [0] * (len(s) + 1)

        if len(s) < 2:
            return 1

        dp[0] = 1
        if s[1] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(dp)):
            if 0 < int(s[i - 1:i]):
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:  # does not count string like "01, 05"
                dp[i] += dp[i - 2]
        return dp[-1]
