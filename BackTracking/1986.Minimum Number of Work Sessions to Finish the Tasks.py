# Time: O(N!) loosely estimate
class Solution:
	def minSessions(self, tasks: List[int], sessionTime: int) -> int:
		self.res = float('inf')
		self.sessionTime = sessionTime

		def dfs(tasks, start, sessions, numberOfsession):
			n = len(tasks)

			if start == n:
				self.res = min(self.res, numberOfsession)
				return

			# PRUNE
			if numberOfsession >= self.res:
				return

			# try to assign current task (i.e. tasks[i]) to old sessions
			for i in range(numberOfsession):
				# can be assigned to certain old sessions
				if sessions[i] + tasks[start] <= self.sessionTime:
					sessions[i] += tasks[start]
					dfs(tasks, start + 1, sessions, numberOfsession)
					sessions[i] -= tasks[start]

			# CANNOT assigned current task (i.e. tasks[i]) to old sessions
			# So, assign it to a new session
			sessions[numberOfsession] += tasks[start]
			dfs(tasks, start + 1, sessions, numberOfsession + 1)
			sessions[numberOfsession] -= tasks[start]

		# sort reversely, so the max task can be assigned to session as earlier as possible.
		# Then we can prune as early as possible i.e. reach termination condition
		tasks.sort(reverse=True)
		n = len(tasks)
		dfs(tasks, 0, [0] * n, 0)
		return self.res


