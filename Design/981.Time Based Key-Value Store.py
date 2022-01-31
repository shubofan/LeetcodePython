import collections


class TimeMap:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.db = collections.defaultdict(list)

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.db[key] += [(timestamp, value)]

	def get(self, key: str, timestamp: int) -> str:
		if key not in self.db:
			return ''
		else:
			lst = self.db[key]
			l, r = 0, len(lst) - 1
			# largest element <= time
			while l < r:
				mid = (l + r + 1) // 2
				if lst[mid][0] <= timestamp:
					l = mid
				else:
					r = mid - 1
			if lst[l][0] <= timestamp:
				return lst[l][1]
			else:
				return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)