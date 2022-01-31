import collections


class Solution:
	def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
		d = collections.defaultdict(list)  # skill, [people]
		for idx, lst in enumerate(people):
			for s in lst:
				d[s] += [idx]
		self.team = [i for i in range(len(people))]

		# req_skills.sort()
		# print(d)
		def dfs(d, req_skills, candidate):

			if not req_skills:
				# print(self.team, candidate)
				if len(candidate) < len(self.team):
					self.team = candidate[:]
				return
			if len(candidate) >= len(self.team):
				return

			s = req_skills.pop()

			for p in d[s]:
				if p in candidate:
					continue
				candidate += [p]
				p_skills = people[p]
				removed_set = set()
				for ps in p_skills:
					if ps in req_skills:
						removed_set.add(ps)
						req_skills.remove(ps)
				dfs(d, req_skills, candidate)
				for ps in removed_set:
					req_skills.add(ps)
				candidate.pop()

			req_skills.add(s)

		dfs(d, set(req_skills), [])
		return self.team