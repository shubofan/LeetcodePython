# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
	# Time O(max(M,N)), M is size of l1 and N is size of l2
	# Space O(M + N), s1 takes O(M), s2 takes O(N)
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		size1, size2 = 0, 0
		s1, s2 = [], []

		cur = l1
		while cur:
			s1 += [cur]
			cur = cur.next

		cur = l2
		while cur:
			s2 += [cur]
			cur = cur.next

		cur = None
		carry = 0
		while s1 or s2 or carry:
			op1, op2 = 0, 0
			if s1:
				op1 = s1.pop().val
			if s2:
				op2 = s2.pop().val
			sum_ = op1 + op2 + carry
			carry = sum_ // 10
			node = ListNode(sum_ % 10)
			node.next = cur
			cur = node
		return cur

