# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        cur = head
        pre = dummy

        # dummy -> 1 -> 2-> 3, cur = 1, pre = dummy
        while cur and cur.next:
            # tmp = 3, keep the next position of cur
            tmp = cur.next.next
            # dummy -> 2
            pre.next = cur.next
            # 2 -> 1
            cur.next.next = cur
            # 1-> 3
            cur.next = tmp

            # dummy -> 2 -> 1-> 3
            # move pre to 1
            pre = cur
            # move cur to 3
            cur = cur.next
        return dummy.next
