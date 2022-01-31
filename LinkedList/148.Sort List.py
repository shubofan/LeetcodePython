# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Space Complexity: (logn) , where n is the number of nodes in linked list. Since the problem is recursive, we need additional space to store the recursive call stack.
# maximum depth of the recursion tree is logn
# Time Complexity: (nlogn),
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fst, slo, pre = head, head, None

        while fst and fst.next:
            pre = slo
            slo = slo.next
            fst = fst.next.next

        pre.next = None

        left = self.sortList(head)
        right = self.sortList(slo)

        return self.merge(left, right)

    def merge(self, l, r):
        dummy = ListNode(-1)
        cur = dummy
        while l and r:
            if l.val <= r.val:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                cur.next = r
                cur = cur.next
                r = r.next
        while l:
            cur.next = l
            cur = cur.next
            l = l.next

        while r:
            cur.next = r
            cur = cur.next
            r = r.next
        return dummy.next