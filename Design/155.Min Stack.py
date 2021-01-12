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

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
