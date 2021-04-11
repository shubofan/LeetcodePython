
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        cur = head
        stack = []
        while cur:
            if cur.child:
                # don't put None to stack
                if cur.next:
                    stack += [cur.next]
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            elif not cur.next and stack:
                tem = stack.pop()
                cur.next = tem
                tem.prev = cur
            cur = cur.next
        return head
