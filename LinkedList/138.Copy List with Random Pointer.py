"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Time: O(n), space O(n)
class Solution:
        def copyRandomList(self, head: 'Node') -> 'Node':
            dic = {} # {node: copied Node}
            cur = head

            if not cur:
                return cur

            pre = None
            while cur:
                node = Node(cur.val)
                dic[cur]=node
                if not pre:
                    pre = node
                else:
                    pre.next = node
                    pre = node
                cur = cur.next

            cur = head
            while cur:
                if cur.random:
                    dic[cur].random = dic[cur.random]
                cur = cur.next
            return dic[head]

# Time: O(n), space O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        cur = head
        if not cur:
            return cur

        # A->A'->B->B'
        while cur:
            node = Node(cur.val)
            tem = cur.next
            cur.next = node
            node.next = tem
            cur = tem

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        l1, l2 = head, head.next
        new_head = l2

        # un-interweave A -> A'-> B -> B'
        # to A -> B and A` -> B'
        while l1.next.next:
            l1.next = l1.next.next
            l2.next = l2.next.next
            l1 = l1.next
            l2 = l2.next
        l1.next = None
        return new_head
