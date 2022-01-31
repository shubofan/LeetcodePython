class MyQueue:
    # Amortized O(1) for each operation
    def __init__(self):
        self.s1 = []  # stack
        self.s2 = []  # queue. All the elements in s2 are FIFO

    def push(self, x: int) -> None:
        self.s1 += [x]

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2 += [self.s1.pop()]
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()