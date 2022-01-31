class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		self.res = []

		def helper(candidates, target, start, path):
			if target == 0:
				self.res += [path]
			elif target < 0:
				return
			else:
				for i in range(start, len(candidates)):
					helper(candidates, target - candidates[i], i, path + [candidates[i]])

		helper(candidates, target, 0, [])
		return self.res