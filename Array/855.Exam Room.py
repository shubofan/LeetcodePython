import bisect


class ExamRoom:

	def __init__(self, n: int):
		self.n = n
		self.students = []

	"""
	For each pair of adjacent students i and j , the maximum distance to the closest student is d = (j - i) / 2 , 
	achieved in the left-most seat i + d . 
	
	Otherwise, we could also sit in the left-most seat, or the right-most seat. 
	"""
	def seat(self) -> int:
		if not self.students:
			self.students += [0]
			return 0

		dis = self.students[0]
		student = 0
		for i in range(1, len(self.students)):
			cur, pre = self.students[i], self.students[i - 1]
			if (cur - pre) // 2 > dis:
				dis = (cur - pre) // 2
				student = pre + dis

		# Considering the right-most seat is a good candidate or not
		if self.n - 1 - self.students[-1] > dis:
			student = self.n - 1

		# self.students += [student]
		# self.students.sort()
		bisect.insort(self.students, student)
		return student

	def leave(self, p: int) -> None:
		self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)