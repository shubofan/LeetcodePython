# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head:
			return None
		slo = head

		while slo:
			fast = slo
			while fast.next and fast.next.val == slo.val:
				fast = fast.next
			slo.next = fast.next
			slo = slo.next
		return head