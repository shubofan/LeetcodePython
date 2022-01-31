# Definition for singly-linked list.
from typing import List

#  Time complexity : O(Nlogk) where k is the number of linked lists.
#
# We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
# Sum up the merge process and we can get: O(∑log2ki=1N)=O(Nlogk) -> Log K times merge, merge at most take O(N), total O(Nlogk)
#
# Space complexity : O(1)  We can merge two sorted linked lists in O(1)
#
# space.
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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Time complexity : O(Nlogk) where k is the number of linked lists. The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1)time.
There are N nodes in the final linked list. So O(N) * O(LogK)

Space complexity: O(n) Creating a new linked list costs O(n) space.
'''
from heapq import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy

        pq = []

        for idx, lst in enumerate(lists):
            if lst:
                heappush(pq, (lst.val, idx,
                              lst))  # must include index Because: When there is a tie in the first value of the tuple, heapq uses the second value as the tie breaker. But since the second value is an object of ListNode, which has no definition of comparision we get an error.

        while pq:
            val, idx, node = heappop(pq)
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(pq, (node.next.val, idx, node.next))
        return dummy.next

