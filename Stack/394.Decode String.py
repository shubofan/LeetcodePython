class Solution:
    def decodeString(self, s: str) -> str:
        lst = list(s)
        s1, s2 = [], []
        res = ''
        if not lst:
            return res
        repeat = 0

        for i in lst:
            if i.isnumeric():
                repeat = repeat * 10 + int(i)
            elif i == '[':
                # calculate the repeat time before current [
                s2 += [repeat]
                s1 += [i]
                repeat = 0
            elif i == ']':
                tem = ''
                while s1[-1] != '[':
                    tem += s1.pop()
                if s1[-1] == '[':
                    s1.pop()
                s1 += tem[::-1] * s2.pop()
            else:
                s1 += [i]
        return ''.join(s1)


class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        n = 0
        for c in s:
            if c.isdigit():
                n = 10 * n + int(c)
            else:
                if c == '[':
                    stack += [str(n) + '[']
                    n = 0
                elif c == ']':
                    sub = ''
                    while stack and '[' not in stack[-1]:
                        sub += stack.pop()
                    if '[' in stack[-1]:
                        repeat_time = int(stack.pop()[:-1])
                        stack += repeat_time * sub[::-1]
                else:
                    stack += [c]
        return ''.join(stack)
