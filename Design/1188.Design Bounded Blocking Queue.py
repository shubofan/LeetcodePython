import threading, collections


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = collections.deque()
        self.condition = threading.Condition()
        self.count = 0

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        with self.condition:
            while self.count >= self.capacity:
                self.condition.wait()
            self.queue += element,
            self.count += 1
            self.condition.notify()

    def dequeue(self):
        """
        :rtype: int
        """
        print(self.queue)
        with self.condition:
            while self.count == 0:
                self.condition.wait()
            element = self.queue.popleft()
            self.count -= 1
            self.condition.notify()
        return element

    def size(self):
        """
        :rtype: int
        """
        with self.condition:
            return self.count



