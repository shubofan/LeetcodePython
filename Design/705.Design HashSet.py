class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 97
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(-1)

    def insert(self, newValue):
        # if key is not existed, add the new element after the head.
        if not self.exists(newValue):
            self.head.next = Node(newValue, self.head.next)

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        if not self.head.next:
            return False
        else:
            cur = self.head.next
            while cur:
                if cur.value == value:
                    return True
                cur = cur.next
            return False
