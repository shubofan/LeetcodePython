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
                # calculate the repeat time before currect [
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
