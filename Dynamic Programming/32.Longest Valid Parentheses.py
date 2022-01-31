class Solution:
    #     def longestValidParentheses(self, s: str) -> int:
    #         res = 0
    #         # handle such case like (), size is 1 - (-1) = 2
    #         stack = [-1]

    #         for i, c in enumerate(s):

    #             if c == '(': # meet left, put it to stack
    #                 stack += [i]
    #             else: # meet ')', pop the top '('
    #                 stack.pop()
    #                 if not stack: # if stack is empty, put index of ')' to stack
    #                     stack += [i]
    #                 else: # update the res
    #                     res = max(res, i - stack[-1])

    #         return res

    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)

        for i, c in enumerate(s):
            if i == 0:
                continue
            if c == ')':
                if s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                # s[i - 1] = ')'
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = dp[i - 1] + 2

        return max(dp) if dp else 0
