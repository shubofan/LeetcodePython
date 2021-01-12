# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        l1 = self.split(lists, 0, len(lists) - 1)
        return l1

    def split(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if r == l:
            return lists[l]
        mid = (l + r) // 2
        l1 = self.split(lists, l, mid)
        l2 = self.split(lists, mid + 1, r)
        return self.mergeLists(l1, l2)

    def mergeLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

        if l1: cur.next = l1

        if l2: cur.next = l2
        return dummy.next
