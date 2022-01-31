import collections


class SnapshotArray:

	def __init__(self, length: int):
		self.arr = collections.defaultdict(dict)
		self.id = 0

	def set(self, index: int, val: int) -> None:
		self.arr[self.id][index] = val

	def snap(self) -> int:
		self.id += 1
		return self.id - 1

	def get(self, index: int, snap_id: int) -> int:

		while snap_id > 0 and index not in self.arr[snap_id]:
			snap_id -= 1
		if index in self.arr[snap_id]:
			return self.arr[snap_id][index]
		# no index for this snap_id, return default value 0
		return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
