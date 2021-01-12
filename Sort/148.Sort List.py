# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        slo, fst = head, head

        pre = None
        # find the mid point
        while fst and fst.next:
            pre = slo
            slo = slo.next
            fst = fst.next.next

        # since slo will be the new head of right half list, make sure it does not have pre
        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slo)
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next