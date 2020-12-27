# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        slo, fst = dummyHead, dummyHead
        while n > 0:
            fst = fst.next
            n -= 1
        while fst.next:
            slo = slo.next
            fst = fst.next
        slo.next = slo.next.next
        return dummyHead.next
