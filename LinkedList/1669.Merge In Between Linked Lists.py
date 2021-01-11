# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        idx = 0
        fro, to = None, None
        while cur:
            # find the node where list2 to insert from
            if idx == a - 1:
                fro = cur
            # find the node where list2 to append to
            if idx == b:
                to = cur.next
                # remove nodes before to and we can stop traverse whole linked list
                cur.next = None
                break
            idx += 1
            cur = cur.next

        fro.next = list2

        cur = list2
        while cur:
            if cur.next == None:
                cur.next = to
                break
            cur = cur.next
        return list1
