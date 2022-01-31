from typing import List


class Job:
	def __init__(self, start, end, profit):
		self.start = start
		self.end = end
		self.profit = profit


class Solution:
	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		n = len(startTime)
		jobs = []
		for i in range(n):
			jobs += [Job(startTime[i], endTime[i], profit[i])]

		# sort jobs by endTime
		jobs.sort(key=lambda j: j.end)

		# dp[i], max profit
		dp = [0] * n

		dp[0] = jobs[0].profit

		for i in range(1, n):
			profit = jobs[i].profit
			for j in range(i - 1, -1, -1):
				if jobs[j].end <= jobs[i].start:
					profit += dp[j]
					break
			# j = self.search(jobs, i - 1, i)
			# if j != -1:
			#     profit += dp[j]
			dp[i] = max(profit, dp[i - 1])

		return dp[-1]

	def search(self, jobs, r, i):
		l, r = 0, r

		while l < r:
			mid = (l + r + 1) // 2

			if jobs[mid].end > jobs[i].start:
				r = mid - 1
			else:
				l = mid

		if jobs[l].end <= jobs[i].start:
			return l
		else:
			return - 1