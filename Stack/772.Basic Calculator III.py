class Solution:
    def calcaulate(self, s: str):
        s = s.replace(' ', '')
        stack = []
        cur = 0
        sign = '+'
        idx = 0
        while idx < len(s):
            c = s[idx]
            if c.isdigit():
                cur = 10 * cur + int(c)
            if c == '(':
                close = self.find_close_parenthesis(idx, s)
                cur = self.calcaulate(s[idx + 1:close])
                idx = close + 1
                if idx < len(s):
                    c = s[idx]
                else:
                    c = sign

            if c in '+-*/' or idx == len(s) - 1:
                # print(stack, cur, idx)
                if sign == '+':
                    stack += [cur]
                if sign == '-':
                    stack += [-cur]
                if sign == '*':

                    stack += [cur*stack.pop()]
                if sign == '/':
                    stack += [stack.pop()/cur]
                sign = c
                cur = 0
            idx += 1

        res = sum(stack)
        return res


    def find_close_parenthesis(self, i:int, s:str):
        level = 0

        for j in range(i, len(s)):
            if s[j] == '(':
                level += 1
            elif s[j] == ')':
                level -= 1
                if level == 0:
                    return j
        return 0


if __name__ == '__main__':
    o = Solution()
    print(o.calcaulate('2*(5+5*2)/3+(6/2+8)'))
    print(o.calcaulate('(2+6* 3+5- (3*14/7+2)*5)+3'))
    print(o.calcaulate('( 5  * ( 12/2) / (5-2) )'))
    print(o.calcaulate('0'))
