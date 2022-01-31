# Two stacks solution
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack += [x]
        if not self.min or self.min[-1] >= x:
            self.min += [x]

    def pop(self) -> None:
        if self.stack and self.min:
            top = self.stack.pop()
            if top == self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        if self.stack and self.min:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack and self.min:
            return self.min[-1]

# One stacks solution

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    # push a pair (value, min element until current element get pushed)
    def push(self, val: int) -> None:

        if not self.s:
            self.s += [(val, val)]
        else:
            self.s += [(val, min(val, self.s[-1][1]))]

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
