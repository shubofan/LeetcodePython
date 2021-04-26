# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-float('inf'))

        while head:
            top = head.next  # preserve next head
            pre = dummy
            cur = dummy.next
            # find the place
            while cur:
                if head.val > cur.val:
                    pre = cur
                    cur = cur.next
                else:
                    break
            # insert
            pre.next = head
            head.next = cur

            head = top

        return dummy.next
