# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        size = 0
        cur = head

        while cur:
            size += 1
            cur = cur.next

        rotate = k % size

        if rotate == 0:
            return head

        step = size - rotate
        cur, pre = head, None

        while step > 0:
            pre = cur
            cur = cur.next
            step -= 1

        # pre is new tail so that pre.next is None
        pre.next = None

        # find the new head
        new_head = cur

        # link the old tail to old head
        while cur.next:
            cur = cur.next
        cur.next = head

        return new_head
