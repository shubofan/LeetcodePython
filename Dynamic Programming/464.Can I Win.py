from typing import List


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        return self.dfs(['0'] * (maxChoosableInteger + 1), desiredTotal, {})

    # dp[i] == '0' means i is not selected
    # dp[i] == '1' means i is selected
    def dfs(self, dp: List[int], desiredTotal: int, dic: dict) -> bool:
        # get current status of selection
        key = "".join(dp)
        # if there is a result, return it
        if key in dic:
            return dic[key]
        # check each number
        for i in range(1, len(dp)):
            # if i has not been selected
            if dp[i] == '0':
                # select it!
                dp[i] = '1'
                # if i >= desiredTotal -> win or opponent lose after i was selected
                if i >= desiredTotal or not self.dfs(dp, desiredTotal - i, dic):
                    # for this key, we can we. memorize it !
                    dic[key] = True
                    # reset and backtrack
                    dp[i] = '0'
                    return True
                # reset and backtrack
                dp[i] = '0'
                # tried all the possible value of  'i', still cannot win, return false
        dic[key] = False
        return False
