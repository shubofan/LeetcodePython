# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        cur = head
        l, r = None, None
        rhead = r
        lhead = l
        while cur:
            if cur.val < x:
                if not l:
                    lhead = cur
                    l = cur
                else:
                    l.next = cur
                    l = cur
            else:
                if not r:
                    rhead = cur
                    r = cur
                else:
                    r.next = cur
                    r = cur
            cur = cur.next
        if l:
            l.next = rhead
        if r:
            r.next = None
        if lhead:
            return lhead
        else:
            return rhead
