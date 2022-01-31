import collections
from collections import OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.cnt = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cnt[key] += 1
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            self.cnt[key] += 1
            return

        if len(self.cache) == self.capacity:
            candidates = self.getLeast()
            for k, v in self.cache.items():
                if k in candidates:
                    self.cnt.pop(k)
                    self.cache.pop(k)
                    break

        self.cache[key] = value
        self.cnt[key] = 1

    def getLeast(self) -> list[int]:
        res = []

        least = float('inf')

        for k, v in self.cnt.items():
            if v == least:
                res += [k]
            elif v < least:
                least = v
                res.clear()
                res += [k]
        return res

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




################## Double linked list #####################

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.fre = 1
        self.pre = None
        self.next = None


class DList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def insert_before_tail(self, node):
        node.next = self.tail
        node.pre = self.tail.pre
        node.pre.next = node
        self.tail.pre = node
        self.size += 1

    def delete_after_head(self):
        if self.size == 0:
            return

        tem = self.head.next
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        self.size -= 1
        return tem


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}  # <k:node of value>
        self.freMap = collections.defaultdict(DList)  # <fre: list of node with same frequency>
        self.min_fre = 0  # minimum frequency
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        fre = node.fre

        # remove the node with old frequency
        node.next.pre = node.pre
        node.pre.next = node.next
        self.freMap[fre].size -= 1

        # update min frequency if necessary
        if self.freMap[fre].size == 0:
            self.freMap.pop(fre)
            if self.min_fre == fre:
                self.min_fre = fre + 1

        # add the node with new frequency
        node.fre += 1
        self.freMap[fre + 1].insert_before_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # key already exists, update with new value and increment the frequency
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            fre = node.fre

            # remove the node with old frequency
            node.next.pre = node.pre
            node.pre.next = node.next
            self.freMap[fre].size -= 1

            # update min frequency if necessary
            if self.freMap[fre].size == 0:
                self.freMap.pop(fre)
                if self.min_fre == fre:
                    self.min_fre = fre + 1

            # add the node with new frequency
            node.fre += 1
            self.freMap[fre + 1].insert_before_tail(node)
        else:
            # need to evict from cache
            if self.size == self.capacity:
                self.size -= 1
                # remove end of minimum frequency
                node_to_be_deleted = self.freMap[self.min_fre].delete_after_head()

                self.nodeMap.pop(node_to_be_deleted.key)
                if self.freMap[self.min_fre].size == 0:
                    self.freMap.pop(self.min_fre)

            # add new node, and set minimum frequency to 1
            self.size += 1
            node = Node(key, value)
            self.nodeMap[key] = node
            self.freMap[1].insert_before_tail(node)
            self.min_fre = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)