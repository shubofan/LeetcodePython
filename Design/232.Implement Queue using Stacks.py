class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.stack += [x]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2 += [self.stack.pop()]

        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        pop = self.pop()
        self.stack2 += [pop]
        return pop

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0 and len(self.stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()