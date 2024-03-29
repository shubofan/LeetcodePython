# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #         if not l1 or not l2:
    #             return l1 or l2
    #         if l1.val < l2.val:
    #             l1.next = self.mergeTwoLists(l1.next, l2)
    #             return l1
    #         else:
    #             l2.next = self.mergeTwoLists(l1, l2.next)
    #             return l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
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