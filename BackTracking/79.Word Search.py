# Time Complexity: O(N⋅3^L) where N is the number of cells in the board and L is the length of the word to be matched.
# For the backtracking function, initially we could have at most 4 directions to explore, but further the choices are reduced into 3 (since we won't go back to where we come from).
# As a result, the execution trace AFTER the FIRST STEP could be visualized as a 3-ary tree, each of the branches represent a potential exploration in the corresponding direction.
# Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree, which is about 3L.


# Space Complexity: O(L) where L is the length of the word to be matched.
# The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is O(L)


class Solution:
	def exist(self, grid, s):
		if not grid or not grid[0]:
			return len(s) == 0

		m, n = len(grid), len(grid[0])
		seen = set()
		for x in range(m):
			for y in range(n):
				if grid[x][y] == s[0]:
					seen.add((x, y))
					if self.dfs(grid, x, y, seen, s[1:]):
						return True
					seen.remove((x, y))
		return False

	def dfs(self, grid, x, y, seen, s):
		m, n = len(grid), len(grid[0])
		if not s:
			return True
		directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

		for dirs in directions:
			x_next, y_next = x + dirs[0], y + dirs[1]
			if 0 <= x_next < m and 0 <= y_next < n and (x_next, y_next) not in seen and grid[x_next][y_next] == s[0]:
				seen.add((x_next, y_next))
				if self.dfs(grid, x_next, y_next, seen, s[1:]):
					return True
				seen.remove((x_next, y_next))
		return False
