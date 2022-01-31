class Solution:
    def calculate(self, s: str) -> int:
        sign, res, cur = 1, 0 , 0
        stack = []
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if c == '+':
                    res += sign * cur
                    cur = 0
                    sign = 1
                if c == '-':
                    res += sign * cur
                    cur = 0
                    sign = -1
                if c == '(':
                    stack += [(sign, res)]
                    res = 0
                    sign = 1
                if c == ')':
                    res += sign * cur
                    sign, cur = stack.pop()
                    res = res *sign + cur
                    cur = 0
                    sign = 1
        return res + cur * sign