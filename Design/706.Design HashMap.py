class Node:
	def __init__(self, k, v, next=None):
		self.k = k
		self.v = v
		self.next = next


class MyHashMap:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.arr = [None] * 97

	def put(self, key: int, value: int) -> None:
		"""
		value will always be non-negative.
		"""
		hash_key = key % 97
		node = Node(key, value)
		# Set head
		if not self.arr[hash_key]:
			self.arr[hash_key] = node
		else:
			cur = self.arr[hash_key]
			while cur:
				# key already exists, upate key, value
				if cur.k == key:
					cur.v = value
					return
				# if not the tail, move ahead
				if cur.next:
					cur = cur.next
				else:
					# find the tail, append new node after tail
					cur.next = node
					return

	def get(self, key: int) -> int:
		"""
		Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
		"""
		hash_key = key % 97
		cur = self.arr[hash_key]
		while cur:
			if cur.k == key:
				return cur.v
			cur = cur.next
		return -1

	def remove(self, key: int) -> None:
		"""
		Removes the mapping of the specified value key if this map contains a mapping for the key
		"""
		hash_key = key % 97
		cur = self.arr[hash_key]
		pre = None
		while cur:
			# find the node to be removed
			if cur.k == key:
				# cur is head, and it will be deleted, make cur.next the new head
				if not pre:
					self.arr[hash_key] = cur.next
					return
				else:
					# remove cur
					pre.next = cur.next
					cur.next = None
					return
			else:
				pre = cur
				cur = cur.next
				hash()

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)