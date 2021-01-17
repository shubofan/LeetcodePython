# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        if not head:
            return res
        #         slo = head

        #         while slo:
        #             if slo.val not in G:
        #                 slo = slo.next
        #             else:
        #                 fst = slo
        #                 while fst and fst.next and fst.next.val in G:
        #                     fst = fst.next
        #                 res += 1
        #                 if fst:
        #                     slo = fst.next

        #         return res
        s = set(G)
        cur = head

        while cur:
            if cur.val in s and not cur.next:
                res += 1
            elif cur.val in s and cur.next.val not in s:
                res += 1
            cur = cur.next
        return res