# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    # Reservoir Sampling :  sample k elements from an population of unknown size
    # For ith element, keep it with probability 1/k, keep old element with probability (k-1)/k
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        keep = None
        cur = self.head

        while cur:
            count += 1
            # 1/k probability
            rand = random.randint(1, count)
            if count == rand:
                keep = cur
            cur = cur.next
        return keep.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()