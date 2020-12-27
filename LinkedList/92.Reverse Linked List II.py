# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        slo = dummy
        pre_slo = None
        # m = 2, n = 4
        # d -> 1 -> 2 -> 3 -> 4 -> 5
        while m > 0:
            pre_slo = slo
            slo = slo.next
            n -= 1
            m -= 1

        # cur = 2 pre = 1
        cur = slo
        pre = pre_slo

        while n >= 0:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
            n -= 1
        # m = 2, n = 4
        # d -> 1 <- 2 <- 3 <- 4  5
        # cur = 5 pre = 4

        pre_slo.next = pre  # 1 -> 4, so  d -> 1 -> 4 -> 3 -> 2  5
        slo.next = cur  # 2 -> 5, d -> 1 -> 4 -> 3 -> 2 -> 5
        return dummy.next
