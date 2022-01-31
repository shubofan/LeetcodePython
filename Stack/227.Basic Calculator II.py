class Solution:
    def calculate(self, s):
        num, stack, op = 0, [], "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack += [num]
                if op == '-':
                    stack += [-num]
                if op == '*':
                    stack += [stack.pop() * num]
                if op == '/':
                    stack += [int(stack.pop() / num)]
                op = c
                num = 0

        return sum(stack)

    def represent(self, input, n):
        return
