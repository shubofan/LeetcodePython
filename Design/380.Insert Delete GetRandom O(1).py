import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # it takes O(1) to access dic and O(1) to append to end of a array list
        self.lst = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:  # O(1)
            self.dic[val] = len(self.lst)  # O(1)
            self.lst += [val]  # O(1)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # cannot delete directly, since it takes O(N), but delete last element takes O(1)
        if val in self.dic:
            # swap index of element to be deleted and last
            idx = self.dic[val]
            self.dic[self.lst[-1]] = idx
            self.lst[-1], self.lst[idx] = self.lst[idx], self.lst[-1]
            self.dic.pop(val)
            self.lst.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()