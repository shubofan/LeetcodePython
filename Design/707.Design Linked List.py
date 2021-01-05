class ListNode:
    def __init__(self, val=-1, pre=None, next=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.pre = pre
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.size:
            return -1
        cur = self.head

        while index >= 0:
            index -= 1
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        first_element = self.head.next
        node = ListNode(val)
        self.head.next = node
        node.pre = self.head
        node.next = first_element
        first_element.pre = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        old_last = self.tail.pre
        node = ListNode(val)
        node.next = self.tail
        self.tail.pre = node
        node.pre = old_last
        old_last.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            while index >= 0:
                cur = cur.next
                index -= 1

            node = ListNode(val)
            node.pre = cur.pre
            node.next = cur
            cur.pre.next = node
            cur.pre = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        else:
            cur = self.head
            while index >= 0:
                cur = cur.next
                index -= 1

            prevNode = cur.pre
            nextNode = cur.next
            nextNode.pre = prevNode
            prevNode.next = nextNode
            cur.pre = None
            cur.next = None
            self.size -= 1
