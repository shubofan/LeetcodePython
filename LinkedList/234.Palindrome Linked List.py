# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slo, fst = head, head

        while fst and fst.next:
            slo = slo.next
            fst = fst.next.next

        # if size of linkedlist is odd, move forward slw
        if fst:
            slo = slo.next

        # reverse 2nd half of linked list
        pre = None
        while slo:
            tem = slo.next
            slo.next = pre
            pre = slo
            slo = tem

        # At this time pre is head of new 2nd half
        cur = head
        while cur and pre:
            if cur.val != pre.val:
                return False
            else:
                cur = cur.next
                pre = pre.next
        return True
