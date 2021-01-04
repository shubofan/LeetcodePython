# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #         O(n) time, O(n) Space
        #         lst = []

        #         cur = head
        #         while cur:
        #             lst += [cur]
        #             cur = cur.next

        #         l, r = 0, len(lst) - 1

        #         dummy = ListNode(-1)
        #         dummy.next = head
        #         cur = dummy
        #         while l < r:
        #             cur.next = lst[l]
        #             cur = cur.next
        #             cur.next = lst[r]
        #             cur = cur.next
        #             l += 1
        #             r -= 1
        #         if l == r:
        #             cur.next = lst[l]
        #             cur = cur.next
        #         cur.next = None

        # O(n) time, O(1) Space
        cur = head
        pre = None
        slo, fst = cur, cur
        if not cur:
            return

            # find the mid
        while fst and fst.next:
            pre = slo
            slo = slo.next
            fst = fst.next.next

        # slo it mid
        cur = slo
        if pre:
            pre.next = None
        pre = None

        # reverse 2nd half 1 - 2 - 3 - 4 - 5 becomes to 1 - 2 - None,  5 - 4 - 3 - None
        while cur:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem

        # merge 2 lists, cur1 is head of 1st half , cur2 is head of 2nd half
        cur1, cur2 = head, pre

        # if len of list is odd, cur2(3 - 4 - 5) is one more node than cur1(1 - 2)
        while cur1 and cur2:
            tem1 = cur1.next
            tem2 = cur2.next

            cur1.next = cur2
            cur1 = tem1
            cur2.next = cur1
            cur2 = tem2

        # last node left in 2nd half like 3 in 5 - 4 - 3 , in this case current list is 1 - 5 - 2 - 4, hence we need
        # to append 3 after 4
        if cur2:
            cur = head
            while cur:
                if not cur.next:
                    cur.next = cur2
                    break
                cur = cur.next
