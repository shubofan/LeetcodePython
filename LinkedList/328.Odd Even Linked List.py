# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even = head
        odd_h = head.next

        odd = odd_h
        isEven = True
        cur = head

        while cur:
            tem = cur.next
            if isEven:
                even.next = cur
                even = cur
                isEven = False
            else:
                odd.next = cur
                odd = cur
                isEven = True
            cur = tem

        odd.next = None
        even.next = odd_h
        return head

