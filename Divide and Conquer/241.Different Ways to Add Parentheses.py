class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        if expression.isdigit():
            return [int(expression)]

        for i, char in enumerate(expression):
            if char in '+-*':
                # divide against operand
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                # merge the result left and right
                for l in left:
                    for r in right:
                        if char == '+':
                            res += [l + r]
                        if char == '-':
                            res += [l - r]
                        if char == '*':
                            res += [l * r]
        return res