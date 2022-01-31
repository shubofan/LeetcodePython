# Time: O(K^N) for each task, we can asign to 1 of K workers, so k * k *k ....*k = (K^N)
# Space: O(K) assignment array
class Solution:
	def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
		self.res = float('inf')

		def dfs(jobs, start, k, assignment):
			n = len(jobs)
			if start == n:  # all n jobs have been assigned. find max working time among works
				self.res = min(self.res, max(assignment))
				return

			# 1st PRUNE
			if max(assignment) > self.res:  # if certain worker's total working time has already > self.res, stop.
				return

			for j in range(k):
				# 2nd PRUNE: for current job, if two worker j and j - 1 has same total working time, there is NO difference assign j or j - 1
				if j > 0 and assignment[j] == assignment[j - 1]:
					continue
				assignment[j] += jobs[start]
				dfs(jobs, start + 1, k, assignment)
				assignment[j] -= jobs[start]

		jobs.sort()
		dfs(jobs, 0, k, [0] * k)

		return self.res
