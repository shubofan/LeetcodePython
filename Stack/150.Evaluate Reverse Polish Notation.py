class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        if not tokens:
            return res
        stack = []
        for token in tokens:
            if token.lstrip('-+').isnumeric():
                stack += [int(token)]
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    stack += [op1 + op2]
                if token == '-':
                    stack += [op2 - op1]
                if token == '*':
                    stack += [op1 * op2]
                if token == '/':
                    stack += [int(op2 / op1)]
        return stack.pop()