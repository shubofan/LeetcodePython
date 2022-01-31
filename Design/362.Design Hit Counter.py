import collections


class HitCounter:
	def __init__(self):
		self.q = collections.deque()

	def hit(self, timeStamp):
		self.q += [timeStamp]

	# Return the number of hits in the past 5 min
	# Time Complexity: O(n)
	def getHits(self, timeStamp):
		while self.q and timeStamp - self.q[0] >= 300:
			self.q.popleft()
		return len(self.q)


# Follow up:
#  What if the number of hits per second could be very large? Does your design scale?
class HitCounter:
	def __init__(self):
		self.times = [-1] * 300 #  check whether the previously saved time stamp in this position is the same as the current time stamp
		self.hits = [0] * 300

	def hit(self, timeStamp):
		idx = timeStamp%300
		if self.times[idx] != timeStamp: # not same, update timestamp in position idx and hits[idx] is 1
			self.times[idx] = timeStamp
			self.hits[idx] = 1
		else: # same timestamp, just increment
			self.hits[idx] += 1


	# Return the number of hits in the past 5 min
	# Time Complexity: O(1)
	def getHits(self, timeStamp):
		res = 0
		for i in range(300):
			if timeStamp - self.times[i] < 300:
				res += self.hits[i]

		return res



if __name__ == '__main__':
	counter = HitCounter()
	counter.hit(1)


	counter.hit(2)

	counter.hit(3)

	 # should return 3.
	counter.getHits(4)


	counter.hit(300)


	 # should return 4.
	counter.getHits(300)

	 # should return 3.
	counter.getHits(301)


