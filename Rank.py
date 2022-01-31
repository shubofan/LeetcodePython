# import unittest
#
#
# class rank:
# 	def __init__(self, user_map={}):
# 		self.user_map = user_map
#
# 	def has_mutual_rank(self, user):
# 		if user in self.user_map and self.user_map[user]:
# 			target = self.user_map[user][0]
# 			if target in self.user_map and self.user_map[target]:
# 				return user == self.user_map[target][0]
#
# 		return False
#
# 	def has_mutual_rank_2(self, user, rank):
# 		if user in self.user_map and rank < len(self.user_map[user]):
# 			target = self.user_map[user][rank]
# 			if target in self.user_map and rank < len(self.user_map[target]):
# 				return user == self.user_map[target][rank]
#
# 		return False
#
#
# 	def change_pair(self, user, idx):
# 		previous = set()
# 		after_change =set()
# 		for rank, mutual in enumerate(self.user_map[user]):
# 			if user in self.user_map[mutual] and rank < len(self.user_map[mutual]) and self.user_map[mutual][rank] == user:
# 				previous.add(mutual)
# 		print(previous)
#
# 		#
# 		# if idx < len(self.user_map[user]):
# 		# 	self.user_map[user][idx-1], self.user_map[user][idx] = self.user_map[user][idx], self.user_map[user][idx - 1]
#
# 		for rank, mutual in enumerate(self.user_map[user]):
# 			if rank == idx - 1:
# 				if user in self.user_map[mutual] and rank + 1 < len(self.user_map[mutual]) and self.user_map[mutual][rank + 1] == user:
# 					after_change.add(mutual)
# 			if rank == idx:
# 				if user in self.user_map[mutual] and rank - 1 < len(self.user_map[mutual]) and self.user_map[mutual][rank - 1] == user:
# 					after_change.add(mutual)
# 		print(after_change)
# 		return previous.intersection(after_change) # depends , ask interview !
#
#
#
#
# class TestClass(unittest.TestCase):
# 	def __init__(self, *args, **kwargs):
# 		super(TestClass, self).__init__(*args, **kwargs)
# 		self.r  = rank()
#
# 	def test_has_mutual_rank(self):
# 		self.r.user_map = {'a': ['c', 'd'], 'c': ['a']}
# 		self.assertTrue(self.r.has_mutual_rank('a'))
#
# 		self.r.user_map = {'a': ['c', 'd'], 'c': ['a'], 'd': ['a']}
# 		self.assertFalse(self.r.has_mutual_rank('d'))
#
# 		self.r.user_map = {'a': ['d', 'c'], 'c': ['a']}
# 		self.assertFalse(self.r.has_mutual_rank('a'))
#
# 		self.r.user_map = {'a': ['d', 'e'], 'c': ['a']}
# 		self.assertFalse(self.r.has_mutual_rank('e'))
#
# 		self.r.user_map = {'a': ['c', 'd'], 'b': ['d', 'a', 'c'], 'c': ['a', 'b'], 'd': ['c', 'a', 'b']}
# 		self.assertTrue(self.r.has_mutual_rank('a'))
# 		self.assertFalse(self.r.has_mutual_rank('b'))
#
# 		self.r.user_map = {}
# 		self.assertFalse(self.r.has_mutual_rank('e'))
#
# 	def test_has_mutual_rank_2(self):
# 		self.r.user_map = {'a': ['c', 'd'], 'c': ['a']}
# 		self.assertTrue(self.r.has_mutual_rank_2('a', 0))
#
# 		self.r.user_map = {'a': ['c', 'd'], 'b': ['a', 'c'], 'c': ['b'], 'd': ['c','a']}
# 		self.assertTrue(self.r.has_mutual_rank_2('d', 1))
# 		self.assertTrue(self.r.has_mutual_rank_2('a', 1))
#
# 		self.assertFalse(self.r.has_mutual_rank_2('a', 0))
# 		self.assertFalse(self.r.has_mutual_rank_2('a', 4))
# 		self.assertFalse(self.r.has_mutual_rank_2('b', 1))
# 		self.assertFalse(self.r.has_mutual_rank_2('k', 4))
#
# 		self.r.user_map = {'a': ['c', 'd'], 'b': ['d', 'a', 'c'], 'c': ['a', 'b'], 'd': ['c', 'a', 'b']}
# 		self.assertTrue(self.r.has_mutual_rank_2('a', 0))
# 		self.assertTrue(self.r.has_mutual_rank_2('a', 1))
#
#
# 	def test_change_pair(self):
# 		self.r.user_map = {'a': ['b', 'c', 'd'], 'b': ['a', 'c', 'd'],'c': ['d', 'a'], 'd': ['a', 'c']}
# 		print(self.r.change_pair('c', 1))
#
# 		self.r.user_map = {'a': ['b', 'c', 'd'], 'b': ['a', 'c'], 'c': ['d', 'a'], 'd': ['c', 'b']}
# 		print(self.r.change_pair('a', 1))
#
# 		self.r.user_map = {'a': ['b', 'c', 'd'], 'b': ['a', 'c'], 'c': ['d', 'a'], 'd': ['c', 'b']}
# 		print(self.r.change_pair('a', 2))

# def sad():
# 	print("a")
#
# if __name__ == '__main__':
#     sad()