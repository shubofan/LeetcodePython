# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def sortedListToBST(self, head: ListNode) -> TreeNode:
		slo, fst = head, head
		pre = None

		if not slo:
			return None
		if not slo.next:
			return TreeNode(slo.val)

		# find the mid point. i.e. slo
		while fst and fst.next:
			pre = slo
			slo = slo.next
			fst = fst.next.next

		root = TreeNode(slo.val)

		# get the left part of linked list: [head, mid)
		pre.next = None
		root.left = self.sortedListToBST(head)

		# get the right part of linked list: [mid.next, tail]
		tem = slo.next
		slo.next = None
		root.right = self.sortedListToBST(tem)
		return root
