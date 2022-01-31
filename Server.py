import unittest


class Server:
	def compute_penalty(self, log: str, time:int):
		loglst = log.split(' ')

		n = len(loglst)

		total_penalty = 0
		if not loglst:
			return total_penalty

		if time < 0:
			return total_penalty

		for i in range(len(loglst)):
			if i < time and loglst[i] == '1':
				total_penalty += 1
			if i >= time and loglst[i] == '0':
				total_penalty += 1
		return total_penalty

	# Ask what if there will be multiple removal time
	def find_best_removal_time(self, log: str):
		n = len(log)

		res = -1
		total_penalty = float('inf')

		for time in range(0, n + 1):
			if self.compute_penalty(log, time) < total_penalty:
				res = time
				total_penalty = self.compute_penalty(log, time)
		return res


	def find_best_removal_times(self, logfile: str):
		logfile = logfile.replace('\n', '')
		lst = logfile.split(' ')
		logs = []

		stack = []
		tmp = []
		print(lst)
		for s in lst:
			if s != 'END':
				stack += [s]
			else:
				while stack and stack[-1] != 'BEGIN':
					tmp += stack.pop()
				stack.pop() # pop start
				logs.append(' '.join(tmp[:][::-1]))
				tmp = []


		res = []
		print(logs)
		for log in logs:
			if log: # log could be ''
				res += [self.find_best_removal_time(log)]
		return  res

class TestClass(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestClass, self).__init__(*args, **kwargs)
		self.s = Server()


	def test_compute_penalty(self):
		self.assertEqual(self.s.compute_penalty('0 0 1 0', -1), 0)

		self.assertEqual(self.s.compute_penalty('0 0 1 0', 0), 3)
		self.assertEqual(self.s.compute_penalty('0 0 1 0', 1), 2)
		self.assertEqual(self.s.compute_penalty('0 0 1 0', 2), 1)
		self.assertEqual(self.s.compute_penalty('0 0 1 0', 3), 2)
		self.assertEqual(self.s.compute_penalty('0 0 1 0', 4), 1)

		self.assertEqual(self.s.compute_penalty('0 0 1 0', 5), 1)

	def test_compute_penalty2(self):
		self.assertEqual(self.s.compute_penalty('0 0 1 1', -1), 0)

		self.assertEqual(self.s.compute_penalty('0 0 1 1', 0), 2)
		self.assertEqual(self.s.compute_penalty('0 0 1 1', 1), 1)
		self.assertEqual(self.s.compute_penalty('0 0 1 1', 2), 0)
		self.assertEqual(self.s.compute_penalty('0 0 1 1', 3), 1)
		self.assertEqual(self.s.compute_penalty('0 0 1 1', 4), 2)

		self.assertEqual(self.s.compute_penalty('0 0 1 1', 5), 2)

	def test_find_best_removal_time(self):
		self.assertEqual(self.s.find_best_removal_time('0 0 1 0'), 2)
		self.assertEqual(self.s.find_best_removal_time('0 0 1 1'), 2)
		self.assertEqual(self.s.find_best_removal_time('1 1 1 0'), 0)

	def test_find_best_removal_times(self):

		print(self.s.find_best_removal_times('BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN'))
		print(self.s.find_best_removal_times('BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END BEGIN BEGIN 0 0 1 1 END BEGIN END'))
		print(self.s.find_best_removal_times('BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END \nBEGIN BEGIN 0 0 1 0 END BEGIN END'))

		print(self.s.find_best_removal_times('BEGIN BEGIN 1 0 0 END 0 0 0 1 BEGIN 1 1 1 0 END'))
		print(self.s.find_best_removal_times('BEGIN END BEGIN BEGIN 1 0 0 END END 0 0 1'))

