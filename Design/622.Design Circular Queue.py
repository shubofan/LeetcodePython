class MyCircularQueue:
    # queue is between [q[head_idx%k], q[tail_idx%k]]
    # tail_index = (self.head_idx + self.count - 1) % k
    def __init__(self, k: int):
        self.count = 0  # total size of current q
        self.q = [-1] * k
        self.head_idx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        idx = (self.head_idx + self.count) % len(self.q)
        self.q[idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head_idx] = -1
        self.head_idx = (self.head_idx + 1) % len(self.q)
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.head_idx + self.count - 1) % len(self.q)]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.q)


if __name__ == '__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    param_1 = obj.enQueue(1)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()
