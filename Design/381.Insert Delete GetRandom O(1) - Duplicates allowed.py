import collections
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.dic = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lst += [val]
        self.dic[val].add(len(self.lst) - 1)
        return len(self.dic[val]) == 1

    def remove(self, val: int) -> bool:

        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.dic:
            idx, last = self.dic[val].pop(), self.lst[-1]
            self.lst[idx] = last
            self.dic[last].add(idx)
            self.dic[last].discard(len(self.lst) - 1)
            self.lst.pop()
            if not self.dic[val]:
                self.dic.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()