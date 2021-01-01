class MyCircularQueue:

    def __init__(self, k: int):
        self._k = k
        self._circularQueue = []

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._circularQueue += [value]
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._circularQueue.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._circularQueue[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._circularQueue[-1]

    def isEmpty(self) -> bool:
        return len(self._circularQueue) == 0

    def isFull(self) -> bool:
        return len(self._circularQueue) == self._k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()