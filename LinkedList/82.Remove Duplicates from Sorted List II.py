class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		cur = head
		if not cur:
			return None

		dummy = ListNode(-1)
		dummy.next = head
		pre = dummy

		while cur:
			if cur.next and cur.val == cur.next.val:
				while cur.next and cur.val == cur.next.val:
					cur = cur.next
				pre.next = cur.next
			else:
				pre = cur
			cur = cur.next
		return dummy.next