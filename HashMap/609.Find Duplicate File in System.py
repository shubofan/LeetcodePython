class Solution:
	def findDuplicate(self, paths: List[str]) -> List[List[str]]:
		d = collections.defaultdict(list)

		for path in paths:
			lst = path.split(' ')
			root = lst[0]

			for i in range(1, len(lst)):
				file = lst[i].split('(')

				name = file[0]
				content = file[1]

				d[content] += [root + '/' + name]
		res = []
		for content, file_paths in d.items():
			if len(file_paths) > 1:
				res += [file_paths]
		return res