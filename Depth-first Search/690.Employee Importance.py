class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
	def getImportance(self, employees: List['Employee'], id: int) -> int:
		res = 0
		dic = {}
		for e in employees:
			dic[e.id] = e

		stack = [dic[id]]
		while stack:
			top = stack.pop()
			res += top.importance
			for sub in top.subordinates:
				stack += [dic[sub]]

		return res