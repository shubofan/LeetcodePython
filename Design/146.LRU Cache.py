import collections

class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.cache = collections.OrderedDict()

	def get(self, key: int) -> int:
		if key in self.cache:
			val = self.cache.pop(key)
			self.cache[key] = val
			return val
		return -1

	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			self.cache.pop(key)
		elif len(self.cache) >= self.capacity:
			self.cache.popitem(last=False)
		self.cache[key] = value

# Hashmao + double linked list
class Node:
	def __init__(self, key: int, val: int):
		self.val = val
		self.key = key
		self.next = None
		self.pre = None


class LRUCache:

	def __init__(self, capacity: int):
		self.size = 0
		self.capacity = capacity
		self.cache = {}
		self.head = Node(-1, -1)
		self.tail = Node(-1, -1)
		self.head.next = self.tail
		self.tail.pre = self.head

	def get(self, key: int) -> int:
		if key not in self.cache:
			return -1

		# remove old node
		old_node = self.cache[key]
		val = old_node.val
		old_node.pre.next = old_node.next
		old_node.next.pre = old_node.pre
		old_node.next, old_node.pre = None, None

		# add new node to tail
		new_node = Node(key, val)
		self.cache[key] = new_node
		self.tail.pre.next = new_node
		new_node.pre = self.tail.pre
		self.tail.pre = new_node
		new_node.next = self.tail
		return val

	def put(self, key: int, val: int) -> None:
		# remove old node
		if key in self.cache:
			cur = self.cache[key]
			cur.pre.next = cur.next
			cur.next.pre = cur.pre
			cur.next, cur.pre = None, None
			self.size -= 1
		# remove first node from head
		elif self.size == self.capacity:
			self.size -= 1
			tem = self.head.next
			self.head.next = tem.next
			tem.next.pre = self.head
			tem.next, tem.pre = None, None
			self.cache.pop(tem.key)

		node = Node(key, val)
		self.tail.pre.next = node
		node.pre = self.tail.pre
		self.tail.pre = node
		node.next = self.tail
		self.cache[key] = node
		self.size += 1
