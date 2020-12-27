# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #     def reverseList(self, head: ListNode) -> ListNode:
    #         cur = head
    #         if not cur:
    #             return
    #         pre = None

    #         while cur:
    #             tem = cur.next
    #             cur.next = pre
    #             pre = cur
    #             cur = tem
    #         return pre

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head)

    def reverse(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur = self.reverse(
            head.next)  # start backtracking from last not. At this time, cur is the last node of linked list
        head.next.next = head  # head -> cur && head <- cur
        head.next = None  # head <- cur
        return cur
