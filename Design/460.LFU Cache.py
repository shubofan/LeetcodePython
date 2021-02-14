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