from typing import List


class Solution:
	# space O(1), array is fixed size of 26
	# time O(N), traverse  [tasks] list takes O(N)
	def leastInterval(self, tasks: List[str], n: int) -> int:
		task_fre = [0] * 26
		for task in tasks:
			task_fre[ord(task) - ord('A')] += 1

		# sort by frequency
		task_fre.sort()

		most_fre = task_fre.pop()

		# ["A","A","A","B","B","B"], n = 2
		# A idle idle A idle idle A -> 4 idles
		total_idle_time = (most_fre - 1) * n

		while task_fre and total_idle_time >= 0:
			# at most assign most_fre-1 to idle, if we have multiple tasks with same frequency like AAABBB, we need to choose most_fre - 1
			total_idle_time -= min(most_fre - 1, task_fre.pop())

		# idle time should always >= 0
		return len(tasks) + max(0, total_idle_time)